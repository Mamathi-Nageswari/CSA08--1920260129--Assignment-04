"""Task 1 - the original script (path changed to the local file so that it runs)."""
f = open("mess_oct.txt")
data = f.read()
total = 0
report = ""
for line in data.split("\n"):
    try:
        parts = line.split(",")
        total = total + int(parts[2])
        report = report + parts[1] + " " + parts[2] + "\n"
    except:
        pass
print(report)
print("Total", total)
