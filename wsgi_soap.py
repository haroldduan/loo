# -*- coding: utf-8 -*-
# Copyright 2019 AVATech
#
# Author Harold.Duan
# This module is python's wsgi function adapted to Apache soap server

from ladon.server.wsgi import LadonWSGIApplication
application = LadonWSGIApplication(['soap'],['./apps/soap.py'])