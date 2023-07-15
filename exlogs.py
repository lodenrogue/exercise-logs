#! /usr/bin/env python3

from datetime import datetime
import argparse
import sys

EXERCISE_LOGS_FILE_PATH = "."


def print_logs():
    with open(f'{EXERCISE_LOGS_FILE_PATH}/exercise_logs.csv', "r") as f:
        print(f.read().strip())


def log_exercise(minutes, description):
    with open(f'{EXERCISE_LOGS_FILE_PATH}/exercise_logs.csv', "a") as f:
        date = datetime.now().strftime("%Y-%m-%d")
        f.write(f'{date},{minutes},"{description}"\n')


def run():
    if len(sys.argv) == 1:
        print_logs()
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("minutes", help="exercise minutes")
        parser.add_argument("-d", default="", help="excercise description")

        args = parser.parse_args()
        log_exercise(args.minutes, args.d)


if __name__ == '__main__':
    run()

