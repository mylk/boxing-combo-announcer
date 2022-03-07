#!/bin/python

import argparse
import random
from subprocess import run
import time

def random_int(limit=6):
    return random.randint(1, limit)

def main():
    total_punches = random_int(args.max_punches)

    punches = []
    for i in range(total_punches):
        punches.append(str(random_int()))

    punches_string = ' '.join(punches)

    print(punches_string)
    run(['espeak', '-s{}'.format(args.speech_speed), punches_string], capture_output=True)
    time.sleep(args.wait_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-punches', '-m', type=int, default=3, help='Maximum number of punches in a combo')
    parser.add_argument('--repetitions', '-r', type=int, default=5, help='Number of combos')
    parser.add_argument('--speech-speed', '-s', type=int, default=140, help='Speed of the announcer')
    parser.add_argument('--wait-time', '-w', type=int, default=4, help='Waiting time between combos')
    args = parser.parse_args()

    for i in range(args.repetitions):
        main()

