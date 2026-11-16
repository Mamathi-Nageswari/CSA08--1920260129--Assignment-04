"""Task 3 - complete try / except / else / finally and raise ... from."""
import os
from attendance_errors import InvalidRecord, parse_line


class AttendanceFileError(Exception):
    """Raised when a whole attendance file cannot be processed."""


def process_file(path):
    f = None
    try:
        f = open(path, encoding="utf-8")
        lines = f.read().splitlines()
        if not lines:
            raise AttendanceFileError(f"{path}: empty file")
    except FileNotFoundError as e:
        raise AttendanceFileError(f"{path}: missing file") from e
    except PermissionError as e:
        raise AttendanceFileError(f"{path}: permission denied") from e
    except UnicodeDecodeError as e:
        raise AttendanceFileError(f"{path}: not UTF-8") from e
    else:
        good, bad = [], []
        for n, line in enumerate(lines, 1):
            try:
                good.append(parse_line(line))
            except InvalidRecord as e:
                bad.append((n, str(e)))
        return good, bad
    finally:
        if f:
            f.close()
        print(f"   finally: {path} closed")


open("ok.csv", "w").write("192311001,2026-10-08,P\n192311002,2026-10-08,X\n")
open("empty.csv", "w").close()
open("latin.csv", "wb").write("192311001,2026-10-08,P \xe9\n".encode("latin-1"))
open("locked.csv", "w").write("x"); os.chmod("locked.csv", 0)
for name in ("ok.csv", "missing.csv", "empty.csv", "latin.csv", "locked.csv"):
    try:
        print(name, "->", process_file(name))
    except AttendanceFileError as e:
        print(name, "->", e, "| cause:", type(e.__cause__).__name__ if e.__cause__ else None)
os.chmod("locked.csv", 0o644)
for n in ("ok.csv", "empty.csv", "latin.csv", "locked.csv"):
    os.remove(n)
