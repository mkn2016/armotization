#!/usr/bin/python3.5
from datetime import timedelta
from calendar import isleap, monthrange

import pandas as pd
from numpy import arange
from pandas.tseries.offsets import MonthBegin, YearBegin, Day

class PeriodSequence(object):
	"""docstring for PeriodSequence"""
	def __init__(self, start_date, period, interval):
		self._start_date = start_date
		self._period = period
		self._interval = interval

	@property
	def _today(self):
		return self._start_date

	@property
	def _date(self) -> int:
		return self._today.day

	@property
	def _month(self) -> int:
		return self._today.month

	@property
	def _year(self) -> int:
		return self._today.year

	def determine_anchor_point(self, day_determinant:int, month_determinant:int, year_determinant:int) -> str:
		days_in_month = monthrange(year_determinant, month_determinant)[1]

		if day_determinant == days_in_month:
			return "{anchor_point}".format(anchor_point="MonthEnd Offset")
		elif day_determinant == 1:
			return "{anchor_point}".format(anchor_point="MonthBegin Offset")
		elif 1 < day_determinant < days_in_month:
			return "{anchor_point}".format(anchor_point="None Anchor Point")
	
	def parse_dates(self):
		_date_ranges = None
		
		if self.determine_anchor_point(self._date, self._month, self._year) == "MonthBegin Offset":
			if self._interval == "Annualy":
				if self._month == 1:
					_date_ranges =  pd.date_range(self._today, periods=self._period * 1, freq="AS-JAN")
				elif self._month == 2:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-FEB")
				elif self._month == 3:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-MAR")
				elif self._month == 4:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-APR")
				elif self._month == 5:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-FEB")
				elif self._month == 6:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-JUN")
				elif self._month == 7:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-JUL")
				elif self._month == 8:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-AUG")
				elif self._month == 9:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-SEP")
				elif self._month == 10:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-OCT")
				elif self._month == 11:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-NOV")
				elif self._month == 12:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="AS-DEC")
			elif self._interval == "Semi-Annualy":
				_date_ranges = pd.date_range(self._today, periods=self._period*2, freq="6MS")
			elif self._interval == "Quarterly":
				if self._month == 1:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-JAN")
				elif self._month == 2:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-FEB")
				elif self._month == 3:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-APR")
				elif self._month == 5:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-MAY")
				elif self._month == 6:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-JUN")
				elif self._month == 7:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-JUL")
				elif self._month == 8:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-AUG")
				elif self._month == 9:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-SEP")
				elif self._month == 10:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-OCT")
				elif self._month == 11:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-NOV")
				elif self._month == 12:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="QS-DEC")
			elif self._interval == "Monthly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 12, freq="MS")
			elif self._interval == "Semi-Monthly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 24, freq="SMS")
			elif self._interval == "Bi-Weekly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 26, freq="14D")
			elif self._interval == "Weekly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 52, freq="7D")
		elif self.determine_anchor_point(self._date, self._month, self._year) == "MonthEnd Offset":
			if self._interval == "Annualy":
				if self._month == 1:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-JAN")
				elif self._month == 2:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-FEB")
				elif self._month == 3:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-MAR")
				elif self._month == 4:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-APR")
				elif self._month == 5:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-MAY")
				elif self._month == 6:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-JUN")
				elif self._month == 7:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-JUL")
				elif self._month == 8:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-AUG")
				elif self._month == 9:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-SEP")
				elif self._month == 10:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-OCT")
				elif self._month == 11:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-NOV")
				elif self._month == 12:
					_date_ranges = pd.date_range(self._today, periods=self._period * 1, freq="A-DEC")
			elif self._interval == "Semi-Annualy":
				_date_ranges = pd.date_range(self._today, periods=self._period * 2, freq="6M")		
			elif self._interval == "Quarterly":
				if self._month == 1:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-JAN")
				elif self._month == 2:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-FEB")
				elif self._month == 3:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-MAR")
				elif self._month == 4:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-APR")
				elif self._month == 5:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-MAY")
				elif self._month == 6:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-JUN")
				elif self._month == 7:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-JUL")
				elif self._month == 8:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-AUG")
				elif self._month == 9:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-SEP")
				elif self._month == 10:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-OCT")
				elif self._month == 11:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-NOV")
				elif self._month == 12:
					_date_ranges = pd.date_range(self._today, periods=self._period * 4, freq="Q-DEC")
			elif self._interval == "Monthly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 12, freq="M")
			elif self._interval == "Semi-Monthly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 24, freq="SM")
			elif self._interval == "Bi-Weekly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 26, freq="14D")
			elif self._interval == "Weekly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 52, freq="7D")
		elif self.determine_anchor_point(self._date, self._month, self._year) == "None Anchor Point":
			if self._interval == "Annualy":
				if self._month == 1:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=1) + Day(self._date - 1)
				elif self._month == 2:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=2) + Day(self._date - 1)
				elif self._month == 3:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=3) + Day(self._date - 1)
				elif self._month == 4:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=4) + Day(self._date - 1)
				elif self._month == 5:
					dates = pd.date_range(self._today, periods=self._period*1, freq="AS")
					_date_ranges = dates - YearBegin(month=5) + Day(self._date - 1)
				elif self._month == 6:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=6) + Day(self._date - 1)
				elif self._month == 7:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=7) + Day(self._date - 1)
				elif self._month == 8:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=8) + Day(self._date - 1)
				elif self._month == 9:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=9) + Day(self._date - 1)
				elif self._month == 10:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=10) + Day(self._date -1 )
				elif self._month == 11:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=11) + Day(self._date -1 )
				elif self._month == 12:
					dates = pd.date_range(self._today, periods=self._period * 1, freq="AS")
					_date_ranges = dates - YearBegin(month=12) + Day(self._date - 1)
			elif self._interval == "Semi-Annualy":
				dates = pd.date_range(self._today, periods=self._period * 2, freq="6MS")
				_date_ranges = dates - MonthBegin(n=1) + Day(self._date - 1)
			elif self._interval == "Quarterly":
				dates = pd.date_range(self._today, periods=self._period * 4, freq="3MS")
				_date_ranges = dates - MonthBegin(n=1) + Day(self._date - 1)
			elif self._interval == "Monthly":
				dates = pd.date_range(self._today, periods=self._period * 12, freq="MS")
				_date_ranges = dates - MonthBegin(n=1) + Day(self._date - 1)
			elif self._interval == "Semi-Monthly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 24, freq="15D")
			elif self._interval == "Bi-Weekly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 26, freq="14D")
			elif self._interval == "Weekly":
				_date_ranges = pd.date_range(self._today, periods=self._period * 52, freq="7D")
		
		return "---" if _date_ranges is None else pd.Series(data=_date_ranges.strftime("%d-%m-%Y"), index=arange(1, len(_date_ranges) + 1))