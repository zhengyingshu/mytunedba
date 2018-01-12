#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: oracleutils.py
@time: 1/10/2018 8:15 PM
"""

import cx_Oracle
from utils import confutils
import pandas as pd
import datetime
from os.path import dirname,abspath
import os

class connoracle(object):
	def __init__(self):
		#获取当前路径
		pwd = dirname(abspath(__file__))
		conf = confutils.myconf(os.path.join(pwd, 'connstring.ini'))
		user = conf.get_str('ORACLE_CONN', 'user')
		password = conf.get_str('ORACLE_CONN', 'password')
		host = conf.get_str('ORACLE_CONN', 'host')
		listenername = conf.get_str('ORACLE_CONN', 'listener')
		#拼接字符串
		connstr = user+'/'+password + '@' + host + '/' + listenername
		self.conn = cx_Oracle.connect(connstr)

	def get_data(self, sql):
		try:
			result = pd.read_sql(sql, self.conn)
			return result
		except cx_Oracle.DatabaseError as msg:
			print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Failed to execute [' + sql + ']')
			print(msg)
			self.conn.close()

	def get_target(self):
		try:
			sql = "select (select value from v$parameter where name = 'db_cache_size') as db_cache_size,\
       						(select value from v$parameter where name = 'db_keep_cache_size') as db_keep_cache_size,\
       						(select value from v$parameter where name = 'db_recycle_cache_size') as db_recycle_cache_size,\
       						(select value from v$parameter where name = 'fast_start_mttr_target') as fast_start_mttr_target,\
       						(select value from v$parameter where name = 'archive_lag_target') as archive_lag_target,\
       						(select value from v$parameter where name = 'db_file_multiblock_read_count') as db_file_multiblock_read_count,\
       						(select round(VALUE, 2)\
       						from GV$SYSMETRIC t\
       						where METRIC_NAME in  ('Response Time Per Txn')) as repose_time\
							from dual"
			result = pd.read_sql(sql, self.conn)
			return result
		except cx_Oracle.DatabaseError as msg:
			print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Failed to execute target sql')
			print(msg)
			self.conn.close()

	def exec_sql(self, sql):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' finish ' + 'execute [' + sql + ']')
		except cx_Oracle.DatabaseError as msg:
			print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Failed to execute [' + sql + ']')
			print(msg)
			cursor.close()
			self.conn.close()

if __name__ == '__main__':
	#print("select * \
	#							  from a_inv_io")
	conoracle = connoracle()
	# data = conoracle.get_data("select * from a_inv_io")
	# print(data.columns)
	#进行alter system 测试
	# connoracle = connoracle()
	# connoracle.exec_sql("alter system set db_cache_size=4M")
	data = conoracle.get_target()
	print(data)


