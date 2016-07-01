#!/usr/bin/python


n = 200
m = 5
data_size = 200

if __name__ == "__main__":
	for pipes in (1, 2, 5, 10, 20):
		fname = "analysis/%dnodes.%dMB.%dpipes.ana"%(n, data_size, pipes)
		inf = open(fname)
		lines = inf.readlines()
		inf.close()
		vis = [[0.0 for x in range(pipes+1)] for x in range(n+m+1)]
		for line in lines:
			line = line.split(' ')
			while '' in line:
				line.remove('')
			part_no = int(line[1])
			if part_no > pipes:
				print "Overflow part_no in: ", fname
				print "At line: ", lines.index(line)
			vis[int(line[0])][part_no] += 1
		for i in range(2, n+m):
			for j in range(1, pipes+1):
				if vis[i][j] > 1:
					print "Duplicated part_no in: ", fname
					print "At node %d with part_no %d of %d times." % (i, j, vis[i][j])
				if vis[i][j] < 1:
					print "Missing part_no in: ", fname
					print "At node %d with part_no %d of %d times." % (i, j, vis[i][j])
	print "All is OK"

