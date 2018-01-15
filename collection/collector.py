#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: collector.py
@time: 1/12/2018 2:57 PM
"""

from utils import oracleutils, mysqlutils
import time
from threading import Thread, Lock, Condition

class Collector(Thread):
	def __init__(self, lock):
		Thread.__init__(self)
		self._l = lock
		self.conoracle = oracleutils.connoracle()
		self.conmysql = mysqlutils.connmysql()

	def collectiondata(self):
		while True:
			#获取目标数据
			self._l.acquire()
			data = self.conoracle.get_target()
			#插入到mysql数据库中
			self.conmysql.insert_data(data, 'tuneinfo')
			self._l.notify_all()
			self._l.release()
			time.sleep(60)

if __name__ == '__main__':
	lock = Condition()
	collector = Collector(lock)
	collector.collectiondata()

