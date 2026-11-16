"""(c) three modules in one folder."""
import sys
import reader, stats, report

recs = reader.read_records(sys.argv[1] if len(sys.argv) > 1 else "../data/october.csv")
print(report.report(stats.percentage(recs), stats.absent_three_days(recs)))
