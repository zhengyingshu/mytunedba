#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: getchangeparam.py
@time: 1/11/2018 11:08 AM
"""

from utils import confutils
import configparser
import numpy as np
from os.path import dirname, abspath
import os

class paramconf(object):
	def __init__(self):
		pwd = dirname(abspath(__file__))
		self.conf = confutils.myconf(os.path.join(pwd, 'params.ini'))

	def getparamall(self):
		params = self.conf.get_str('PARAM_MAIN', 'params')
		params = params.split(',')
		return params

	def getparamvalue(self, paramname):
		paramvalue = self.conf.get_str('PARAM_MAIN', paramname)
		paramvalue = paramvalue.split(',')
		return paramvalue

	#获取修改数据库参数的时间间隔
	def getsleeptime(self):
		return self.conf.get_str('CHANGE_TIME', 'sleep_time')

if __name__ == '__main__':
	paramconf = paramconf()
	#获取所有的param参数名
	# params = paramconf.getparamall()
	# print(params[0])
	#获取param的值
	paramvalue = paramconf.getparamvalue('db_cache_size')
	print(paramvalue[0])
	# for param in paramvalue.split(','):
	# 	print(param)

