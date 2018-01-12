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
import threading

if __name__ == '__main__':
	collector = collector.Collector()
	changeparam = changeparam.changeparam()

	threads = []
	t1 = threading.Thread(target=collector.collectiondata())
	threads.append(t1)
	t2 = threading.Thread(target=changeparam.runchange())
	threads.append(t2)

	for t in threads:
		t.setDaemon(True)
		t.start()

	t.join()




