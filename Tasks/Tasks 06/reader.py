"""fest.reader - read registration lines from department files."""
from pathlib import Path

DEPARTMENTS = ["cse", "ece", "eee", "mech", "civil"]


def read_department(folder, dept, errors):
    """Yield (file, line number, text); a missing file is logged, never raised."""
    path = Path(folder, f"{dept}.txt")
    try:
        with path.open(encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if line.strip():
                    yield path.name, n, line.strip()
    except FileNotFoundError:
        errors.append(f"{path.name}: missing department file")
    except UnicodeDecodeError:
        errors.append(f"{path.name}: not UTF-8, skipped")
