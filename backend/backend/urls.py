# -*- coding: utf-8 -*-

from backend.handlers import base


url_patterns = [
    (r"/api/armotization", base.MainHandler),
]