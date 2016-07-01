#!/usr/bin/python

import numpy as np
import pylab as pl

x = [i+1 for i in range(512)]
y1 = []
y2 = []
y3 = []
y4 = []

inf = open("delta/output/multi/fig_data_time", "r")
y1 = inf.readline().split(',')
y2 = inf.readline().split(',')
y3 = inf.readline().split(',')
y4 = inf.readline().split(',')


fig = pl.figure(figsize=(8,6), dpi=100, facecolor='white')

for i in range(512):
	x[i] = x[i]/520.0
	y1[i] = float(y1[i])/330.0
	y2[i] = float(y2[i])/330.0
	y3[i] = float(y3[i])/330.0
	y4[i] = float(y4[i])/330.0
pl.xlim(0, 1)
pl.ylim(0, 1)

font = {'family' : 'serif',
		'color'  : 'black',
		'weight' : 'normal',
		'size'   : 16,
		}

myxlins = []
myxlins.append(0)
myxlins.append(32.0/520.0)
myxlins.append(64.0/520.0)
myxlins.append(128.0/520.0)
myxlins.append(256.0/520.0)
myxlins.append(512.0/520.0)
myxlins.append(1.0)

ax = pl.gca()
#ax.set_xticks(np.linspace(0, 1, 521))
ax.set_xticks(myxlins)
ax.set_xticklabels(('0', '32', '64', '128', '256', '512(files)', ''))
ax.set_yticks(np.linspace(0, 1, 12))
ax.set_yticklabels(('0','30.0','60.0','90.0','120.0','150.0','180.0','210.0','240.0','270.0','300.0','(s)'))
ax.set_xlabel('Number of 1MB-File in X-Updating(MB)',fontdict=font)
ax.set_ylabel('Consumed Time of X-Delta(s)',fontdict=font)

pl.plot(x, y1, 'm-',  linewidth=1, label='Total Time  Seq.Mod')
pl.plot(x, y2, 'y-',  linewidth=1, label='Total Time  Seq.R/A')
pl.plot(x, y3, 'g-',  linewidth=1, label='Total Time  Rand.Mod')
pl.plot(x, y4, 'r-',  linewidth=1, label='Total Time  Rand.R/A')
#pl.plot([0,1],[0.1,0.1], 'r', linewidth = 2);
pl.legend(loc='best')
#pl.grid(True)
pl.title('Time Consuming')
pl.savefig('time-multi.png')
pl.show()
