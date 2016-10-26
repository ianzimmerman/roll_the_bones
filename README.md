# World of Warcraft: Legion, Roll the Bones Tester
Testing and modeling for Legion Rogue Roll the Bones ability.

Python 3 only.

Run & Use:
1) Execute rtb.py from prompt
2) 'r' for roll, 't' for test, 'l' to list buffs, 'x' to exit

Module:
---

from rtb import roll_the_bones, get_bone

result = [get_bone(r)['name'] for r in roll_the_bones()]
print('{}: {}'.format(len(result), ', '.join(result)))
