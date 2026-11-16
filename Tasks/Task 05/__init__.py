"""attendance package: reader, stats and report sub-modules."""
from .reader import read_records
from .stats import percentage, absent_three_days
from .report import report

__all__ = ["read_records", "percentage", "absent_three_days", "report"]
