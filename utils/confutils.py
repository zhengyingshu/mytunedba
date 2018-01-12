#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: confutils.py
@time: 1/10/2018 9:01 PM
"""

import configparser

class myconf(object):
	def __init__(self, configfilepath):
		self.cfg = configparser.ConfigParser()
		self.cfg.read(configfilepath)

	#输入对应的section和type，返回参数值
	def get_str(self, sectionname, typename):
		return self.cfg.get(sectionname, typename)

	#对section进行添加option
	def setsectionvalue(self, sectionname, option, value):
		self.cfg.set(sectionname, option, value)

	#添加section
	def addsection(self, sectionname):
		self.cfg.add_section(sectionname)

if __name__ == '__main__':
	conf = myconf('connstring1.ini')
	print(conf.get_str('ORACLE_CONN', 'user'))
