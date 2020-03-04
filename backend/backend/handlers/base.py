# -*- coding: utf-8 -*-
from datetime import datetime

from tornado.web import RequestHandler

from backend.calculations.base import Base

class BaseRequestHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Server", "---")
        self.set_header("X-Powered_By", "---")
        self.set_header("X-Content-Powered-By", "---")
        self.set_header("X-Frame-Options", "SAMEORIGIN")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST')
        self.set_header("X-Content-Type-Options", "nosniff")
        self.set_header("X-XSS-Protection", "1; mode=block")

class MainHandler(BaseRequestHandler):
    def post(self):
        interval = self.get_argument("interval")
        start_date = self.get_argument("start_date")
        interest_rate = self.get_argument("interest_rate")
        payment_period = self.get_argument("payment_period")
        principal_amount = self.get_argument("principal_amount")

        start_date = datetime.strptime(start_date, "%Y-%m-%d")

        data = Base(int(principal_amount), int(interest_rate), int(payment_period), start_date, interval)
        
        self.write(data.schedule())
