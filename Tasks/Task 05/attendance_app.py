"""(a) one script: reading, statistics and report in one file."""
import sys


def read_records(path):
    with open(path, encoding="utf-8") as f:
        return [tuple(l.strip().split(",")) for l in f if l.count(",") == 2]


def percentage(records):
    c = {}
    for reg, _, s in records:
        p, t = c.get(reg, (0, 0)); c[reg] = (p + (s == "P"), t + 1)
    return {r: 100 * p / t for r, (p, t) in c.items()}


def absent_three_days(records):
    run, flagged = {}, set()
    for reg, _, s in sorted(records, key=lambda x: (x[0], x[1])):
        run[reg] = run.get(reg, 0) + 1 if s == "A" else 0
        if run[reg] >= 3:
            flagged.add(reg)
    return sorted(flagged)


def report(pct, absent):
    lines = [f"{r}  {v:5.1f}%" for r, v in sorted(pct.items())]
    lines.append("absent 3 consecutive days: " + ", ".join(absent))
    return "\n".join(lines)


if __name__ == "__main__":
    recs = read_records(sys.argv[1] if len(sys.argv) > 1 else "../data/october.csv")
    print(report(percentage(recs), absent_three_days(recs)))
