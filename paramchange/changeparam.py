#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: changeparam.py
@time: 1/11/2018 11:39 AM
"""

from paramchange import getchangeparam
from utils import oracleutils
import random
import time


class changeparam(object):
	def __init__(self):
		self.getparamname = getchangeparam.paramconf()
		self.params = self.getparamname.getparamall()
		self.sleeptime = self.getparamname.getsleeptime()
		self.connoracle = oracleutils.connoracle()

	def runchange(self):
		while True:
			#进行休眠时间
			time.sleep(int(self.sleeptime))
			lenparams = len(self.params)
			#随机获取一个参数值
			paramname = self.params[random.randint(0, lenparams-1)].strip()
			#获取参数值
			paramvalues = self.getparamname.getparamvalue(paramname)
			lenparamvalues = len(paramvalues)
			#随机获取一个参数值
			paramvalue = paramvalues[random.randint(0, lenparamvalues-1)].strip()
			sql = "alter system set " + paramname + " = " + paramvalue
			#执行参数修改
			conn = oracleutils.connoracle()
			conn.exec_sql(sql)

if __name__ == '__main__':
	changeparam = changeparam()
	changeparam.runchange()
