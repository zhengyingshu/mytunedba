#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: processdemo.py
@time: 1/15/2018 8:55 PM
"""

from multiprocessing import Process, current_process
import time

def worker():
	while True:
		print('in worker %s' % current_process())
		time.sleep(1)

if __name__ == '__main__':
	ps = [Process(target=worker) for i in range(6)]
	for p in ps:
		p.start()
	for p in ps:
		p.join()

