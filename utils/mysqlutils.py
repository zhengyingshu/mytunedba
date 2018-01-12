#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: mysqlutils.py
@time: 1/10/2018 10:12 PM
"""

import pymysql
import pandas as pd
from utils import confutils
import sys
from sqlalchemy import create_engine
from sqlalchemy import exc
import sqlalchemy
import datetime
from os.path import dirname, abspath
import os

class connmysql(object):
	def __init__(self):
		# 获取当前路径
		pwd = dirname(abspath(__file__))
		conf = confutils.myconf(os.path.join(pwd, 'connstring.ini'))
		user = conf.get_str('MYSQL_CONN', 'user')
		password = conf.get_str('MYSQL_CONN', 'password')
		host = conf.get_str('MYSQL_CONN', 'host')
		dbname = conf.get_str('MYSQL_CONN', 'db')
		charset = conf.get_str('MYSQL_CONN', 'charset')
		port = conf.get_str('MYSQL_CONN', 'port')
		# 拼接字符串
		connstr = 'mysql+pymysql://'+user+':'+password+"@"+host+":"+port+"/"+dbname
		#测试字符串
		#print(connstr)
		try:
			self.conn = pymysql.connect(host=host, user=user, password=password, db=dbname, charset=charset)
		except pymysql.err.OperationalError as e:
			print('Error is ' + str(e))
			self.conn.close()
			sys.exit()
		try:
			self.engine = create_engine(connstr)
		except sqlalchemy.exc.OperationalError as e:
			print('Error is ' + str(e))
			self.conn.close()
			sys.exit()
		except sqlalchemy.exc.InternalError as e:
			print('Error is ' + str(e))
			self.conn.close()
			sys.exit()

	def get_data(self, sql):
		try:
			data = pd.read_sql(sql, con=self.conn)
			return data
		except pymysql.err.ProgrammingError as e:
			print('Error is ' + str(e))
			self.conn.close()
			sys.exit()

	def insert_data(self, data, tablename):
		data.to_sql(name=tablename, con=self.engine, if_exists='append', index=False)
		print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Finish insert data into table : [' + tablename + ']')

if __name__ == '__main__':
	conmysql = connmysql()
	data = conmysql.get_data("select * from mytest")
	print(data)
	conmysql.insert_data(data, 'mytest_copy')
