#!/usr/bin/env python3

import random
import time
from collections import Counter
from operator import itemgetter

def dice_roll(dice=1, sides=6):
    '''
    returns a dice roll generator for number of dice (dice) with (sides) number sides
    '''
    
    n = 0
    while n < dice:
        yield random.randint(1, sides)
        n += 1

def get_bone(bone):
    '''
    returns dictionary of dice info when given an integer dice face number
    '''
    
    buffs = {
        1: { 
            'name': 'Broadsides',
            'spell_id': 193356,
            'description': 'Your combo-generating abilities generate 1 additional combo point.'
        },
        2: { 
            'name': 'Shark Infested Waters',
            'spell_id': 193357,
            'description': 'Critical Strike chance increased by 40%.'
        },
        3: { 
            'name': 'Grand Melee',
            'spell_id': 193358,
            'description': 'Attack speed increased by 40%. Leech increased by 20%.'
        },
        4: { 
            'name': 'True Bearing',
            'spell_id': 193359,
            'description': 'Finishers reduce the remaining cooldown on many of your abilities by 2 sec per combo point.'
        },
        5: { 
            'name': 'Buried Treasure',
            'spell_id': 199600,
            'description': 'Increases Energy regeneration by 40%.'
        },
        6: { 
            'name': 'Jolly Roger',
            'spell_id': 199603,
            'description': 'Saber Slash has an additional 40% chance of striking an additional time.'
        }
    }
    try:
        return buffs[bone]
    except KeyError as e:
        print("Bones must be in range 1 to 6: ", e)
        raise


def roll_the_bones():
    '''
    returns a list of highest rolling dice. 
    e.g. if dice_roll(6) returns [1,4,4,6,6,3] this returns [4,6]
    '''
    
    face             = itemgetter(0)
    roll_count      = itemgetter(1)

    throw           = Counter(dice_roll(6))
    high_roll_count = roll_count(throw.most_common(1)[0])
    
    return [face(roll) for roll in throw.items() if roll_count(roll) == high_roll_count]

def test(rolls=1000):
    '''
    finds percentage of rolls that return 1, 2, 3, or 6 buffs
    '''
    
    start_time = time.time()
    results = {n: 0 for n in [1,2,3,6]}

    for r in range(rolls):
        buffs = len(roll_the_bones())
        results[buffs] += 1

    print('Results for {:,} rolls'.format(rolls))
    for n_buffs, times in results.items():
        print('{} Buff:'.format(n_buffs), '{:.2%}'.format(times/rolls))
    
    print()
    print('Calc time: {:.3} seconds'.format(time.time()-start_time))

if __name__ == '__main__':
    print('Roll (r), test (t), list (l) or exit (x)')
    while True:
        print()
        task = input('').lower().strip()
    
        if task in ['r', 'roll']:
            result = [get_bone(r)['name'] for r in roll_the_bones()]
            print('{}: {}'.format(len(result), ', '.join(result)))
        
        elif task in ['t', 'test']:
            rolls = int(input('Rolls: ').strip())
            test(rolls)
        
        elif task in ['l', 'list']:
            for b in range(1,7):
                r = get_bone(b)
                print("{} ({}): '{}'".format(r['name'], r['spell_id'], r['description']))
        
        elif task in ['x', 'exit']:
            break
        else:
            print('Unknown command: {}'.format(task))
