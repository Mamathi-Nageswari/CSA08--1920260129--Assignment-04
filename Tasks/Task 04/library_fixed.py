"""Task 4.3 - repaired library program: append mode, newlines, with, error log."""
import datetime


def log_error(message):
    with open("errors.log", "a", encoding="utf-8") as err:
        err.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {message}\n")


def save_returns(books, day):
    with open("returns.log", "a", encoding="utf-8") as log:
        for b in books:
            log.write(f"{day},{b}\n")


def process(day_file):
    try:
        with open(day_file, encoding="utf-8") as f:
            books = [line.strip() for line in f if line.strip()]
        save_returns(books, day_file)
    except FileNotFoundError:
        log_error(f"missing day file {day_file}")
    except OSError as e:
        log_error(f"could not save returns from {day_file}: {e}")


if __name__ == "__main__":
    import os
    for name in ("returns.log", "errors.log"):
        if os.path.exists(name):
            os.remove(name)
    for day in ("days/mon.txt", "days/tue.txt", "days/wed.txt", "days/thu.txt"):
        process(day)
    print("returns.log:\n" + open("returns.log").read().rstrip())
    print("errors.log:\n" + open("errors.log").read().rstrip())
