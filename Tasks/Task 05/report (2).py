"""report: formatting the report."""


def report(pct, absent):
    lines = [f"{r}  {v:5.1f}%" for r, v in sorted(pct.items())]
    lines.append("absent 3 consecutive days: " + ", ".join(absent))
    return "\n".join(lines)
