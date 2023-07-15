# Exercise Logs

Log and list exercise times

## Usage

Log minutes for the current day

```
python3 exlogs.py 20
```

Log minutes with a description

```
python3 exlogs.py -d "swimming and walking" 20
```

List exercise times

```
python3 exlogs.py
```

Output:

```
2023-07-14,10,""
2023-07-15,26,"swimming and walking"
```

## Logs file path

Change this line to set the location of your exercise logs file:

```
EXERCISE_LOGS_FILE_PATH = "/path/to/your/file/directory"
```
