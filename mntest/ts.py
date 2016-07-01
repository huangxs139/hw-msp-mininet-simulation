#!/usr/bin/python

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

if __name__ == '__main__':
	for p in range(1, 5):
		tmp = 0
		for i in range(1, p):
			tmp += 1
		for v in range(1, p):
			tmp += 10
		print tmp
