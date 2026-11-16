"""Task 1.2 - repaired mess-bill totaller."""
import sys
from decimal import Decimal, InvalidOperation


def total_mess_bills(filename):
    """Return (lines of the report, total, rejected lines as (line number, text, reason))."""
    total, report, rejected = Decimal("0"), [], []
    with open(filename, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            try:
                reg, name, amount = parts
                amount = Decimal(amount)
            except ValueError:
                rejected.append((line_no, line, f"expected 3 fields, found {len(parts)}"))
                continue
            except InvalidOperation:
                rejected.append((line_no, line, f"amount {parts[2]!r} is not a number"))
                continue
            total += amount
            report.append(f"{reg} {name:<10} {amount:>9.2f}")
    return report, total, rejected


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "mess_oct.txt"
    try:
        report, total, rejected = total_mess_bills(name)
    except FileNotFoundError:
        sys.exit(f"File not found: {name}")
    print("\n".join(report))
    print(f"Total {total:.2f}")
    for line_no, text, reason in rejected:
        print(f"rejected line {line_no}: {text!r} - {reason}")
