#!/usr/bin/python
import re, os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

n = 200
m = 5
data_size = 200
ans_list = []

def solve(n, pipes):
	inf = open("analysis/%dnodes.%dMB.%dpipes.ana"%(n, data_size, pipes), "r")
	lines = inf.readlines()
	inf.close()
	mat = [[[0.0 for k in range(pipes+1)] for j in range(n+m+1)] for i in range(n+m+1)]
	for line in lines:
		line = line.split(' ')
		dest = int(line[0])
		part_no = int(line[1])
		src = int(line[2])
		t = float(line[3])
		mat[src][dest][part_no] += t
	ts = [[0.0 for i in range(pipes+1)] for i in range(n+m+1)]
	for p in range(1, pipes+1):
		ts[1][p] = ts[n][p-1]
		ts[n+1][p] = ts[1][p] + mat[1][n+1][p]
		for i in range(n+2, n+m):
			ts[i][p] = ts[i-1][p] + mat[1][i][p]
		ts[2][p] = ts[n+m-1][p] + mat[1][2][p]
		ts[n][p] = ts[2][p] + mat[1][n][p]
		v = 3
		while v <= 100 and mat[v-1][v][p] > 0:
			ts[v][p] = ts[v-1][p]+mat[v-1][v][p]
			v += 1
		v = n-1
		while v > 1 and mat[v+1][v][p] > 0:
			ts[v][p] = ts[v+1][p]+mat[v+1][v][p]
			v -= 1

	ans = 0
	for i in range(1, n+m):
		for p in range(1, pipes+1):
			ans = (ans if ans > ts[i][p] else ts[i][p])
	ans_list.append(ans)

	ouf = open("ans", "a")
	ouf.write("%d nodes, %d MBytes, %d pipelines, whole time %.5f (s)\n"%(n,data_size,pipes,ans))
	ouf.close()
		



if __name__ == "__main__":
	for n in (100, 200):
		for pipes in (1, 2, 5, 10, 20):
			solve(n, pipes)
	ouf = open("fig_data", "a")
	for i in range(len(ans_list)):
		ouf.write("%.5f"%ans_list[i])
		ouf.write('\n' if (i+1)%5 == 0 else ',')
	ouf.close()
