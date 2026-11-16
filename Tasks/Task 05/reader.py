"""attendance.reader: reading attendance files."""


def read_records(path):
    with open(path, encoding="utf-8") as f:
        return [tuple(l.strip().split(",")) for l in f if l.count(",") == 2]
