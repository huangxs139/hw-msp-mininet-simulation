#!/usr/bin/python
import re, os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

n = 100
m = 5
ans_list = []

def solve(data_size, pipes):
	inf = open("analysis/%dnodes.%dMB.%dpipes.out"%(n, data_size, pipes), "r")
	lines = inf.readlines()
	inf.close()
	mat = [[[0.0 for k in range(pipes+1)] for j in range(n+m+1)] for i in range(n+m+1)]
	for line in lines:
		line = line.split(' ')
		dest = int(line[0])
		part_no = int(line[1])
		src = int(line[2])
		t = float(line[3])
		print src, dest, part_no, data_size, pipes
		mat[src][dest][part_no] += t
	t3 = 0.0
	for i in range(n+1, n+m):
		for p in range(1, pipes+1):
			t3 += mat[1][i][p]
	ts = [[0.0 for i in range(pipes+1)] for i in range(n+1)]
	ts[1][1] = t3
	ts[2][1] = ts[1][1] + mat[1][2][1]
	for p in range(2, pipes+1):
		ts[2][p] = ts[2][p-1] + mat[1][2][p]
	ts[n][1] = ts[2][pipes] + mat[1][n][1]
	for p in range(2, pipes+1):
		ts[n][p] = ts[n][p-1] + mat[1][n][p]
	for p in range(1, pipes+1):
		v = 3
		while mat[v-1][v][p] > 0 and v <= n:
			ts[v][p] = ts[v-1][p] + mat[v-1][v][p]
			v += 1
		v = n-1
		while mat[v+1][v][p] > 0 and v > 1:
			ts[v][p] = ts[v+1][p] + mat[v+1][v][p]
			v -= 1
	ans = t3
	for i in range(1, n):
		for p in range(1, pipes+1):
			ans = (ans if ans > ts[i][p] else ts[i][p])
	ans_list.append(ans)

	ouf = open("ans", "a")
	ouf.write("%d nodes, %d MBytes, %d pipelines, whole time %.5f (s)\n"%(n,data_size,pipes,ans))
	ouf.close()
		



if __name__ == "__main__":
	for pipes in (1, 2, 5, 10, 20):
		for data_size in range(20, 220, 20):
			solve(data_size, pipes)
	ouf = open("fig_data", "a")
	for i in len(ans_list):
		ouf.write("%.5f"%ans_list[i])
		ouf.write('\n' if (i+1)%10 == 0 else ',')
	ouf.close()
