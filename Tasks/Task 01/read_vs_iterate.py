"""Task 1 - Alternative: f.read() / f.readlines() vs iterating line by line, 50,000 lines."""
import os, time, tracemalloc
from mess_total import total_mess_bills

with open("big_mess.txt", "w") as f:
    for i in range(50_000):
        f.write(f"1923{i:05d},Student{i},{1000 + i % 500}.50\n")


def by_read(name):
    with open(name) as f:
        return sum(float(l.split(",")[2]) for l in f.read().split("\n") if l)


def by_readlines(name):
    with open(name) as f:
        return sum(float(l.split(",")[2]) for l in f.readlines())


def by_iteration(name):
    with open(name) as f:
        return sum(float(l.split(",")[2]) for l in f)


print(f"file size {os.path.getsize('big_mess.txt'):,} bytes")
for fn in (by_read, by_readlines, by_iteration):
    tracemalloc.start(); t = time.perf_counter(); fn("big_mess.txt"); t = time.perf_counter() - t
    peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
    print(f"{fn.__name__:13}: {t:.4f} s, peak memory {peak / 1e6:6.2f} MB")
t = time.perf_counter(); _, total, rej = total_mess_bills("big_mess.txt")
print(f"repaired total_mess_bills: {time.perf_counter() - t:.4f} s, total {total}, rejected {len(rej)}")
os.remove("big_mess.txt")
