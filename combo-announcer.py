#!/bin/python

import random
from subprocess import call
import time

max_punches = 3
repetitions = 5
speech_speed = 140
wait_time = 4

def random_int(limit=6):
    return random.randint(1, limit)

def main():
    total_punches = random_int(max_punches)

    punches = []
    for i in range(total_punches):
        punches.append(str(random_int()))

    punches_string = ','.join(punches)

    print(punches_string)
    call(['espeak', '-s{}'.format(speech_speed), punches_string])
    time.sleep(wait_time)

for i in range(repetitions):
    main()

