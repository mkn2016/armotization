#!/usr/bin/python3.5

import json as json
from math import ceil
from collections import OrderedDict
from itertools import zip_longest, repeat
from datetime import timedelta, datetime

from pandas import DataFrame
from numpy import allclose, arange, ipmt, pmt, ppmt, pv, round, append

from backend.calculations.period import PeriodSequence

class Base(PeriodSequence):
	"""docstring for Base"""

	def __init__(self, loan_amount, interest_rate, payment_period,start_date, payment_interval="Monthly"):
		super().__init__(start_date, payment_period, payment_interval)
		self._start_date = start_date
		self._loan_amount = loan_amount
		self._interest_rate = interest_rate
		self._payment_period = payment_period
		self._payment_interval = payment_interval
	
	@property
	def _rate(self) -> float:
		return self._interest_rate / 100

	@property
	def _computing_period(self):
		if self._payment_interval == "Annualy":
			return 1
		elif self._payment_interval == "Semi-Annualy":
			return 2
		elif self._payment_interval == "Quarterly":
			return 4
		elif self._payment_interval == "Monthly":
			return 12
		elif self._payment_interval == "Semi-Monthly":
			return 24
		elif self._payment_interval == "Bi-Weekly":
			return 26
		elif self._payment_interval == "Weekly":
			return 52

	@property
	def _per(self):
		if self._computing_period == 1:
			return arange(self._payment_period * 1) + 1
		elif self._computing_period == 2:
			return arange(self._payment_period * 2) + 1
		elif self._computing_period == 4:
			return arange(self._payment_period * 4) + 1
		elif self._computing_period == 12:
			return arange(self._payment_period * 12) + 1
		elif self._computing_period == 24:
			return arange(self._payment_period * 24) + 1
		elif self._computing_period == 26:
			return arange(self._payment_period * 26) + 1
		elif self._computing_period == 52:
			return arange(self._payment_period * 52) + 1

	@property
	def _interest(self):
		return ipmt(self._rate / self._computing_period, self._per, self._payment_period * self._computing_period, self._loan_amount)

	@property
	def _principal(self):
		return ppmt(self._rate / self._computing_period, self._per, self._payment_period * self._computing_period, self._loan_amount)

	@property
	def _payment(self):
		return pmt(self._rate / self._computing_period, self._payment_period * self._computing_period, self._loan_amount)

	@property
	def _balance(self):
		return pv(self._rate / self._computing_period, self._per, self._payment)[::-1]

	@property
	def _validate_series(self) -> bool:
		return allclose(self._interest + self._principal, self._payment)

	def schedule(self) -> dict:
		round_absolute = lambda value: round(abs(value), 2)

		def initialize_ending_balance(balance_array) -> None:
			ending_balance = balance_array.copy()[1::]
			ending_balance = append(ending_balance, 0)
			return ending_balance
		
		if self._validate_series:
			payment_dates = self.parse_dates()
			payment = round_absolute(self._payment)
			interest = round_absolute(self._interest)
			total_interest = round(sum(interest), 2)
			principal = round_absolute(self._principal)
			beginning_balance = round_absolute(self._balance)
			periodic_payments = list(repeat(payment, len(self._per)))
			ending_balance = round_absolute(initialize_ending_balance(self._balance))
			
			data = []
			for (d, b, e, i, pr, py) in zip_longest(payment_dates, beginning_balance, ending_balance, interest, principal, periodic_payments):
				data.append({"dates": d, "beginning_balance": b, "ending_balance": e, "interest": i, "principal": pr, "periodic_payment": py})
			
			return dict(
				data=data,
				expected_payment=payment,
				total_interest=total_interest,
				expected_start_date=payment_dates[1],
				expected_number_of_payments=len(self._per),
				total_payment=round_absolute(self._loan_amount + total_interest),
				expected_end_date=payment_dates[len(payment_dates) - 0]
			)