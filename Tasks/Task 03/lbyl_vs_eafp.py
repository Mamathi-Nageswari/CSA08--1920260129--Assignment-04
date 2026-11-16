"""Task 3 - Alternative: look before you leap (if checks) vs ask forgiveness (try/except)."""
import timeit
from attendance_errors import InvalidRecord, parse_line


def lbyl(line):
    parts = line.strip().split(",")
    if len(parts) == 3 and parts[2] in ("P", "A"):
        return tuple(parts)
    return None


def eafp(line):
    try:
        return parse_line(line)
    except InvalidRecord:
        return None


good, bad = "192311001,2026-10-08,P", "192311003,2026-10-08"
for share in (0.0, 0.01, 0.5):
    lines = [bad if i < share * 1000 else good for i in range(1000)]
    t1 = timeit.timeit(lambda: [lbyl(l) for l in lines], number=200) / 200 / 1000
    t2 = timeit.timeit(lambda: [eafp(l) for l in lines], number=200) / 200 / 1000
    print(f"bad lines {share:4.0%}: if checks {t1 * 1e9:4.0f} ns/line | try/except {t2 * 1e9:4.0f} ns/line")
