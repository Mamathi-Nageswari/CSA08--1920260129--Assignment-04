"""fest.writer - write master list, event lists, summary and error log."""
from pathlib import Path


def write_all(out_dir, master, errors):
    out = Path(out_dir); out.mkdir(exist_ok=True)
    for old in out.glob("event_*.txt"):
        old.unlink()
    with open(out / "master.csv", "w", encoding="utf-8") as f:
        for s in sorted(master, key=lambda s: s["reg"]):
            f.write(f"{s['reg']},{s['name']},{s['dept']},{s['email']},{';'.join(s['events'])}\n")
    events = {}
    for s in master:
        for e in s["events"]:
            events.setdefault(e, []).append(s)
    for e, people in sorted(events.items()):
        with open(out / f"event_{e.lower()}.txt", "w", encoding="utf-8") as f:
            f.writelines(f"{s['reg']} {s['name']} ({s['dept']})\n" for s in sorted(people, key=lambda s: s["reg"]))
    with open(out / "summary.txt", "w", encoding="utf-8") as f:
        f.write(f"students: {len(master)}\nerrors: {len(errors)}\n")
        f.writelines(f"{e}: {len(p)}\n" for e, p in sorted(events.items()))
    with open(out / "errors.log", "w", encoding="utf-8") as f:
        f.writelines(e + "\n" for e in errors)
