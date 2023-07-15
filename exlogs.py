from datetime import datetime
import argparse

EXERCISE_LOGS_FILE_PATH = "."


def log_exercise(minutes, description):
    with open(f'{EXERCISE_LOGS_FILE_PATH}/exercise_logs.csv', "a") as f:
        date = datetime.now().strftime("%Y-%m-%d")
        f.write(f'{date},{minutes},"{description}"\n')


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("minutes", help="exercise minutes")
    parser.add_argument("-d", default="", help="excercise description")

    args = parser.parse_args()
    log_exercise(args.minutes, args.d)


if __name__ == '__main__':
    run()

