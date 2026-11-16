"""attendance.stats: attendance statistics."""


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
