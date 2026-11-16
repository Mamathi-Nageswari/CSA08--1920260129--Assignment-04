"""Task 3 - Complete the Code: custom exception and safe file summary."""
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when a line of the attendance file is not in the expected format."""


def parse_line(line):
    """'192311001,2026-10-08,P' -> ('192311001', '2026-10-08', 'P')"""
    parts = line.strip().split(",")
    # TODO 1
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    if parts[2] not in ("P", "A"):
        raise InvalidRecord(f"invalid status {parts[2]!r}")
    return tuple(parts)


def summarise(path):
    present, absent, errors = 0, 0, []
    # TODO 2
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            try:
                reg, date, status = parse_line(line)
            except InvalidRecord as e:
                errors.append((line_no, str(e)))
            else:
                if status == "P":
                    present += 1
                else:
                    absent += 1
    return present, absent, errors


if __name__ == "__main__":
    data = ("192311001,2026-10-08,P\n192311002,2026-10-08,A\n"
            "192311003,2026-10-08\n192311004,2026-10-08,L\n")
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(data)
    print(summarise(tmp.name))
    os.remove(tmp.name)

    try:
        print(summarise("no_such_day.csv"))
    except FileNotFoundError as e:
        print("handled:", type(e).__name__, "-", e.filename)
