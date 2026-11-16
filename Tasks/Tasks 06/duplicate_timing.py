"""Task 6 - Alternative: duplicate detection by searching a list vs a set."""
import random, time

for n in (1_000, 10_000, 50_000):
    regs = [str(192300000 + random.randrange(n)) for _ in range(n)]
    t = time.perf_counter(); seen_list, d1 = [], 0
    for r in regs:
        if r in seen_list: d1 += 1
        else: seen_list.append(r)
    tl = time.perf_counter() - t
    t = time.perf_counter(); seen, d2 = set(), 0
    for r in regs:
        if r in seen: d2 += 1
        else: seen.add(r)
    ts = time.perf_counter() - t
    assert d1 == d2
    print(f"{n:>6} registrations: list {tl:7.3f} s | set {ts:7.4f} s | duplicates {d1}")
