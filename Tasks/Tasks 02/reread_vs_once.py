"""Task 2 - Alternative: re-reading all files for each student vs one pass."""
import time
from pathlib import Path
from monthly_attendance import process_month

FOLDER = "attendance/2026-10"


def per_student(folder, students):
    result, reads = {}, 0
    for reg in students:                         # s students
        p = t = 0
        for path in sorted(Path(folder).glob("*.txt")):   # f files
            reads += 1
            for line in path.open():             # l lines
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[0] == reg and parts[2] in ("P", "A"):
                    p += parts[2] == "P"; t += 1
        result[reg] = [p, t]
    return result, reads


t = time.perf_counter(); once, _ = process_month(FOLDER); t1 = time.perf_counter() - t
t = time.perf_counter(); again, reads = per_student(FOLDER, sorted(once)); t2 = time.perf_counter() - t
print("same counts:", once == again)
print(f"one pass   : 20 file reads,  {t1 * 1e3:.2f} ms")
print(f"per student: {reads} file reads, {t2 * 1e3:.2f} ms")
