"""(b) main script importing one module."""
import sys
from attendance_lib import read_records, percentage, absent_three_days, report

recs = read_records(sys.argv[1] if len(sys.argv) > 1 else "../data/october.csv")
print(report(percentage(recs), absent_three_days(recs)))
