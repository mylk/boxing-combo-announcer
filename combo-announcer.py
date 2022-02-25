#!/bin/python

import random
from subprocess import call

def random_int(limit=6):
    return random.randint(1, limit)

total_punches = 3

punches = []
for i in range(total_punches):
    punches.append(str(random_int()))

punches_string = ','.join(punches)

print(punches_string)
call(['espeak', '-s140', punches_string])

