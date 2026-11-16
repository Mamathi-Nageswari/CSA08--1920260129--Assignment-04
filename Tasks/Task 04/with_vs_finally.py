"""Task 4 - Alternative: manual open/close with try/finally vs with; files left open."""
import gc, os, timeit


KEPT = []   # keep references, as a long-running program would (log objects, caches)


class Bad:
    def __str__(self):
        raise OSError("write failed")


def manual_no_finally(name, items):
    f = open(name, "w"); KEPT.append(f)
    for x in items:
        f.write(str(x))
    f.close()
    return f


def manual_finally(name, items):
    f = open(name, "w"); KEPT.append(f)
    try:
        for x in items:
            f.write(str(x))
    finally:
        f.close()


def with_stmt(name, items):
    with open(name, "w") as f:
        KEPT.append(f)
        for x in items:
            f.write(str(x))


gc.disable()
for fn in (manual_no_finally, manual_finally, with_stmt):
    before = len(os.listdir("/proc/self/fd"))
    for i in range(50):
        try:
            fn("tmp.txt", ["a", Bad()])
        except OSError:
            pass
    print(f"{fn.__name__:17}: files left open after 50 failed writes = {len(os.listdir('/proc/self/fd')) - before}")
gc.enable(); gc.collect()
for fn in (manual_finally, with_stmt):
    t = timeit.timeit(lambda: fn("tmp.txt", ["a", "b"]), number=2000) / 2000
    print(f"{fn.__name__:17}: {t * 1e6:.1f} us per open/write/close")
os.remove("tmp.txt")
