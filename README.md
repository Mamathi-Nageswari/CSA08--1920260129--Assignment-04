# CSA08 Python Programming - Assignment 4

- Name: ____________________
- Register number: ____________________
- Python version: Python 3.10.12
- Libraries: standard library only (pathlib, decimal, tempfile, os, time, timeit, tracemalloc, datetime). See requirements.txt.

## How to run
Open a terminal in the task folder and run the command shown.

| Folder | Command | Result |
|---|---|---|
| Task1 | `python3 poor_script.py`, `python3 mess_total.py [file]`, `python3 read_vs_iterate.py` | Old script totals only 1180; repaired total 4741.50 with 2 rejected lines logged |
| Task2 | `python3 monthly_attendance.py [folder]`, `python3 reread_vs_once.py` | Percentages for 20 daily files, below_75.txt and damaged_lines.log written |
| Task3 | `python3 attendance_errors.py`, `python3 processor.py`, `python3 misuse.py`, `python3 lbyl_vs_eafp.py` | Expected output reproduced; missing/empty/non-UTF-8/locked files handled; blanket except hides a NameError |
| Task4 | `python3 test_defects.py`, `python3 library_fixed.py`, `python3 with_vs_finally.py` | Defects shown; repaired log keeps every day, one title per line, errors.log written |
| Task5 | `cd a_one_script && python3 attendance_app.py` (same for `b_module/main.py`, `c_three_modules/main.py`, `d_package/main.py`), `python3 import_cost.py` | Four organisations give the same report including the new 3-consecutive-absence list |
| Task6 | `python3 fest_main.py [input folder] [output folder]`, `python3 duplicate_timing.py` | master.csv, event_*.txt, summary.txt, errors.log written; never stops on bad lines or missing files |

Input files: Task1/mess_oct.txt, Task2/attendance/2026-10/*.txt, Task4/days/*.txt, Task5/data/october.csv, Task6/registrations/*.txt. Screenshots are in each folder's `screenshots/` directory.
