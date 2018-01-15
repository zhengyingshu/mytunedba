#!/usr/bin/python
# encoding:utf8

"""
@author: james shu
@contact: 598546998@qq.com
@file: maincollector.py
@time: 1/12/2018 3:13 PM
"""

from collection import collector
from paramchange import changeparam
from threading import Thread, Condition

if __name__ == '__main__':
	lock = Condition()
	collector = collector.Collector(lock)
	changeparam = changeparam.changeparam()

	threads = []
	t1 = Thread(target=collector.collectiondata)
	threads.append(t1)
	# t3 = Thread(target=collector.collectiondata)
	# threads.append(t3)
	t2 = Thread(target=changeparam.runchange)
	threads.append(t2)

	for t in threads:
		t.setDaemon(True)
		t.start()

	for t in threads:
		t.join()




