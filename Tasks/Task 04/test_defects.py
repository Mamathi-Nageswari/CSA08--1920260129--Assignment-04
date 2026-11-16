"""Task 4.2 - run process() for three days and print the log, showing each defect."""
import library_buggy as lib


class Broken:
    """A book entry whose str() fails, like a write() error part-way through."""
    def __str__(self):
        raise OSError("disk full")


print("Defect 1 and 2: run Mon, Tue, Thu")
for day in ("days/mon.txt", "days/tue.txt", "days/thu.txt"):
    lib.process(day)
print("returns.log =", repr(open("returns.log").read()), "<- only Thursday, and titles joined")
print("\nDefect 3: write() fails part-way")
log = open("returns.log", "w")
try:
    log.write("Gitanjali")
    log.write(str(Broken()))
except OSError as e:
    print("error:", e, "| file still open?", not log.closed, "| nothing logged about the error")
log.close()
print("\nDefect 4: a missing day prints only 'missing' (which file? when?):")
lib.process("days/wed.txt")
