#!/usr/bin/env python3

import random
import time
from collections import Counter
from operator import itemgetter

def dice_roll(n_dice=1, sides=6):
    rolls = list()
    for r in range(n_dice):
        rolls.append(random.randint(1,sides))
    
    return rolls

def get_bone(bone):
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
    die             = itemgetter(0)
    roll_count      = itemgetter(1)

    throw           = Counter(dice_roll(6))
    high_roll_count = roll_count(throw.most_common(1)[0])
    
    return [die(roll) for roll in throw.items() if roll_count(roll) == high_roll_count]

def test(n_rolls):
    start_time = time.time()
    results = {n: 0 for n in [1,2,3,6]}

    for r in range(n_rolls):
        buffs = len(roll_the_bones())
        results[buffs] += 1

    print('| Results for {:,} rolls'.format(n_rolls))
    for n_buffs, times in results.items():
        print('| {} Buff:'.format(n_buffs), '{:.2%}'.format(times/n_rolls))
    
    print('| Calc time: {:.3} seconds'.format(time.time()-start_time))

if __name__ == '__main__':
    while True:
        print()
        task = input('Roll (r), test (t), list (l) or exit (x): ').lower().strip()
    
        if task in ['r', 'roll']:
            result = [get_bone(r)['name'] for r in roll_the_bones()]
            print('{}: {}'.format(len(result), ', '.join(result)))
        
        elif task in ['t', 'test']: 
            test(10000)
        
        elif task in ['l', 'list']:
            for b in range(1,7):
                r = get_bone(b)
                print("{} ({}): '{}'".format(r['name'], r['spell_id'], r['description']))
        
        elif task in ['x', 'exit']:
            break