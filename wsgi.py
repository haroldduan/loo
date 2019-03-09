# -*- coding: utf-8 -*-
# Copyright 2019 AVATech
#
# Author Harold.Duan
# This module is python's wsgi function adapted to Apache http server.

import sys,inspect,os

this_file = inspect.getfile(inspect.currentframe())
dir_path = os.path.abspath(os.path.dirname(this_file))
# print(dir_path)
# load the web api folder insert to sys path
sys.path.insert(0,dir_path)
# sys.path.insert(0,'C:\iWorkSpace\iGits\web_api2b1')
# import app funtion
from __init__ import app as application