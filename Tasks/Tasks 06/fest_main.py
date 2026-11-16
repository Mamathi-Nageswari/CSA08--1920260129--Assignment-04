"""Task 6 - College fest registration desk: python3 fest_main.py [input folder] [output folder]."""
import sys
from fest.reader import DEPARTMENTS, read_department
from fest.validate import BadRegistration, parse
from fest.writer import write_all


def run(in_dir="registrations", out_dir="output"):
    master, seen, errors = [], set(), []
    for dept in DEPARTMENTS:
        for fname, n, line in read_department(in_dir, dept, errors):
            try:
                s = parse(line)
            except BadRegistration as e:
                errors.append(f"{fname}:{n}: {e}")
                continue
            if s["reg"] in seen:                       # O(1) average set lookup
                errors.append(f"{fname}:{n}: duplicate registration {s['reg']}")
                continue
            seen.add(s["reg"]); master.append(s)
    write_all(out_dir, master, errors)
    return master, errors


if __name__ == "__main__":
    run(*sys.argv[1:3])
    for name in ("master.csv", "event_quiz.txt", "summary.txt", "errors.log"):
        print(f"--- output/{name}"); print(open(f"output/{name}").read().rstrip())
