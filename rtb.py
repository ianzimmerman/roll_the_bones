#!/usr/bin/env python3

import random
from collections import Counter

def dice_roll(n_dice=1, sides=6):
    r = 0
    while r < n_dice:
        yield random.randint(1,sides)
        r += 1

def rtb():
    buffs = {
        1: { 
            'name': 'Jolly Roger',
            'spell_id': 199603,
            'description': 'Saber Slash has an additional 40% chance of striking an additional time.'
        },
        2: { 
            'name': 'Grand Melee',
            'spell_id': 193358,
            'description': 'Attack speed increased by 40%. Leech increased by 20%.'
        },
        3: { 
            'name': 'Shark Infested Waters',
            'spell_id': 193357,
            'description': 'Critical Strike chance increased by 40%.'
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
            'name': 'Broadsides',
            'spell_id': 193356,
            'description': 'Your combo-generating abilities generate 1 additional combo point.'
        }
    }

    throw = Counter(dice_roll(6))
    best_roll = throw.most_common(1)[0][1]

    return [buffs[b] for b, n in throw.items() if n == best_roll]

def test(n_rolls):
    results = {n: 0 for n in [1,2,3,6]}
    current_streak, singles_record = 0, 0

    for r in range(n_rolls):
        buffs = len(rtb())
        results[buffs] += 1

        if buffs == 1:
            current_streak += 1
            singles_record = max(singles_record, current_streak)
        else:
            current_streak = 0

    print('---')
    print('Most consecutive singles over {:,} rolls: {}'.format(n_rolls, singles_record))
    for n_buffs, times in results.items():
        print('{} Buff:'.format(n_buffs), '{:.2%}'.format(times/n_rolls))

if __name__ == '__main__':
    for i, r in enumerate(rtb()):
        print("{} {} ({}): '{}'".format(i+1, r['name'], r['spell_id'], r['description']))
    
    test(10000)
