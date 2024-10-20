# Day 1

# Troubleshooting
Today you need to master the following keywords and concepts:
1. Keywords: ls, pwd, cd, mkdir, mv, touch, cat, tail, head, cut, sort


## Prerequisites

1. ```python3 -m venv venv && source venv/bin/activate```
2. ```pip3 install -r requirements.txt```

## Warm up

1. List all the files in a folder
2. Check your present working directory
3. Change to the previous directory and move back to the current one
4. Create a directory and move into it. Create a file named “log_<name>.txt” or “log_<name>.log” in the new directory
5. Move the file to previous directory
6. Move the file back to the original directory

## Task 1

- In the current terminal window, run the application ```day1app.py```. The logs for this app would get stored in ```day1app.log``` file.
- Open a duplicate terminal window (navigate to the same path as day1app.py if a new terminal window was opened)

All further instructions deal with the log file 'day1app.log'
- Print the entire log file in one shot
- Print the first 5 lines of the logfile
- Print the last 5 lines of the logfile
- Print the running log
- Print all errors lines
- Print the errors lines from now on
- Print just the errors and not the entire lines
- *Find the number of errors by error code and sort them in descending order of error count
- *Find the user facing the largest number of errors

Kill the application ```day1app.py```