#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: threaddemo2.py
@time: 1/15/2018 8:14 PM
"""
from threading import Thread, current_thread, Lock
import time

def worker(lock):
	while True:
		lock.acquire()
		print('in worker %s' % current_thread())
		lock.release()
		time.sleep(0.1)

class Mythread(Thread):
	def __init__(self, lock):
		Thread.__init__(self)
		self._lock = lock

	def run(self):
		while True:
			self._lock.acquire()
			print('in worker %s' % current_thread())
			self._lock.release()
			time.sleep(0.1)


if __name__ == '__main__':
	lock = Lock()
	print('in main %s' % current_thread())
	#threads = [Thread(target=worker, args=[lock]) for i in range(5)]
	threads = [Mythread(lock) for i in range(5)]
	for t in threads:
		t.start()

	for t in threads:
		t.join()



