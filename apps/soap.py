# -*- coding: utf-8 -*-
# Copyright 2019, AVATech
#
# Author Harold.Duan
# This module is soap service implements.

from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType

class User(LadonType):
        name = str
        age = int
        groups = [ str ]

class ListUsersResponse(LadonType):
        success = bool
        users = [ User ]

class UserService(object):
        @ladonize(str,rtype=ListUsersResponse)
        def listUsers(self,uid):
                user1 = User()
                user1.name = u"John Doe"
                user1.age = 30
                user1.groups = [ u'admin', u'www-data' ]
                user2 = User()
                user2.name = u"John Deer"
                user2.age = 60
                user2.groups = [ u'farming', u'tractor' ]
                result = ListUsersResponse()
                result.success = True
                result.users = [ user1, user2 ]
                return result

class Calculator(object):
        @ladonize(int,int,rtype=int)
        def add(self,a,b):
                return a+b

# if __name__ == "__main__":
#         try:
#             # import sys,inspect,os
#             # this_file = inspect.getfile(inspect.currentframe())
#             # dir_path = os.path.abspath(os.path.dirname(this_file))
#             # sys.path.insert(0,dir_path)
#             import subprocess
#             #p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#             # for line in p.stdout.readlines():
#             #     print(line)
#             p = subprocess.Popen('ladon-3.7-ctl testserve soap.py -p 7095',
#             shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#             for line in p.stdout.readlines():
#                 print(line)
#         except ImportError as ex:
#             print(ex.msg)