# -*- coding: utf-8 -*-

"""Global settings for the project"""

import os.path

from tornado.options import define


define("port", default=8001, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

__BASE_PACKAGE__ = "backend"

settings = {}

settings["debug"] = True
settings["cookie_secret"] = "Tozp6l3MFqSuyK01PNXXOijW1"
settings["xsrf_cookies"] = False
