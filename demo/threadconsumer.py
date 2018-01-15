#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: threadconsumer.py
@time: 1/15/2018 8:20 PM
"""

from threading import Thread, Condition, current_thread, Lock
import time

class Producer(Thread):
	def __init__(self, datacache, lock):
		Thread.__init__(self)
		self._dc = datacache
		self._l = lock

	def run(self):
		i = 0
		while True:
			msg = 'from producer msg is %d' % i
			self._l.acquire()
			self._dc.append(msg)
			self._l.notify_all()
			self._l.release()
			time.sleep(0.2)
			i += 1

class Consumer(Thread):
	def __init__(self, datacache, lock):
		Thread.__init__(self)
		self._dc = datacache
		self._l = lock

	def run(self):
		while True:
			self._l.acquire()
			while len(self._dc) == 0:
				self._l.wait()
			msg = self._dc.pop()
			self._l.release()
			print('consumer %s recevier' % msg)
			time.sleep(1)

if __name__ == "__main__":
	datacache = []
	lock = Condition()

	producer1 = Producer(datacache, lock)
	producer1.start()

	consumers = [Consumer(datacache, lock) for i in range(8)]
	for c in consumers:
		c.start()

	producer1.join()
	for c in consumers:
		c.join()


