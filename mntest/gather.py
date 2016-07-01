#!/usr/bin/python

import os

n = 200
m = 5
data_size = 200 #MB


def rm(pipes):
	os.system("rm analysis/%dnodes.%dMB.%dpipes.ana"%(n,data_size,pipes))

def solve(dest, pipes):
	ans = []
	src = []
	ts = []
	inf = open("results/%04d/%dnodes.%dMB.%dpipes.out"%(dest,n,data_size,pipes), "r")
	lines = inf.readlines()
	inf.close()
	for line in lines:
		if 'SUM' in line:
			continue
		line = line.split(' ')
		while '' in line:
			line.remove('')
		if "local" in line:
			src.append(int(line[line.index("with")+1].split('.')[3]))
		elif "sec" in line:
			data = float(line[line.index("sec")+1])
			rate = float(line[line.index("MBytes")+1])
			ts.append(data/rate)
		else:
			pass
	for i in range(len(src)):
		ans.append((dest, i+1, src[i], ts[i]))
	ofname = "analysis/%dnodes.%dMB.%dpipes.ana"%(n,data_size,pipes)
	ouf = open(ofname, "a")
	for item in ans:
		ouf.write("%d %d %d %.5f\n" % (item[0], item[1], item[2], item[3]))
	ouf.close()

if __name__ == "__main__":
	for pipes in (1, 2, 5, 10, 20):
		rm(pipes)
	for dest in range(2, n+m):
		for pipes in (1, 2, 5, 10, 20):
			solve(dest, pipes)
