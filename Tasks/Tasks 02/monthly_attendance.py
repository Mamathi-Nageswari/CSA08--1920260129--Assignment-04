"""Task 2 - Monthly attendance from daily biometric files (implements the pseudocode)."""
import sys
from pathlib import Path


def process_month(folder):
    counts = {}                     # register number -> [present, total]
    damaged = []                    # (file name, line number, text)
    for path in sorted(Path(folder).glob("*.txt")):
        with path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                parts = line.strip().split(",")
                if len(parts) != 3 or parts[2] not in ("P", "A"):
                    damaged.append((path.name, line_no, line.strip()))
                    continue
                reg, _, status = parts
                c = counts.setdefault(reg, [0, 0])
                c[0] += status == "P"; c[1] += 1
    return counts, damaged


def write_reports(counts, damaged, out_dir="."):
    with open(Path(out_dir, "below_75.txt"), "w", encoding="utf-8") as out:
        for reg, (p, t) in sorted(counts.items()):
            pct = 100 * p / t
            out.write(f"{reg},{p},{t},{pct:.1f}\n" if pct < 75 else "")
    with open(Path(out_dir, "damaged_lines.log"), "w", encoding="utf-8") as log:
        for name, line_no, text in damaged:
            log.write(f"{name}:{line_no}: {text!r}\n")


if __name__ == "__main__":
    counts, damaged = process_month(sys.argv[1] if len(sys.argv) > 1 else "attendance/2026-10")
    for reg, (p, t) in sorted(counts.items()):
        print(f"{reg}  present {p:2}/{t:2}  {100 * p / t:5.1f}%")
    write_reports(counts, damaged)
    print("below_75.txt:\n" + open("below_75.txt").read().rstrip())
    print("damaged_lines.log:\n" + open("damaged_lines.log").read().rstrip())
