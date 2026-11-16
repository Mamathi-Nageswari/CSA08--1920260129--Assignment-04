"""(d) package attendance/ with sub-modules."""
import sys
import attendance.stats
from attendance import stats
from attendance.stats import percentage
from attendance import read_records, absent_three_days, report

recs = read_records(sys.argv[1] if len(sys.argv) > 1 else "../data/october.csv")
print(report(percentage(recs), absent_three_days(recs)))
print("same function three ways:", attendance.stats.percentage is stats.percentage is percentage)
