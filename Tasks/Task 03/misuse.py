"""Task 3.4 - misuse experiment: except Exception: pass hides a typing error."""
from attendance_errors import parse_line

lines = ["192311001,2026-10-08,P", "192311002,2026-10-08,A", "192311003,2026-10-08,P"]


def count_present_hidden(lines):
    present = 0
    for line in lines:
        try:
            reg, date, status = parse_line(line)
            if status == "P":
                presnt += 1            # typing error in the variable name
        except Exception:
            pass
    return present


def count_present_specific(lines):
    present = 0
    for line in lines:
        reg, date, status = parse_line(line)
        if status == "P":
            presnt += 1
    return present


print("with except Exception: pass ->", count_present_hidden(lines), "(should be 2, no error shown)")
try:
    count_present_specific(lines)
except NameError as e:
    print("without the blanket except  ->", type(e).__name__ + ":", e)
