import sys
from datetime import datetime

EXERCISE_LOGS_FILE_PATH = "."


def log_exercise(minutes):
    with open(f'{EXERCISE_LOGS_FILE_PATH}/exercise_logs.csv', "a") as f:
        date = datetime.now().strftime("%Y-%m-%d")
        f.write(f'{date},{minutes}\n')


def run():
    if len(sys.argv) < 2:
        print("Usage: exlogs <minutes>")
        exit(1)
    else:
        log_exercise(sys.argv[1])

if __name__ == '__main__':
    run()

