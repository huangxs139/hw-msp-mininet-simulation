#!/usr/bin/python

import numpy as np
import pylab as pl

x = [1.0, 2.0, 3.0, 4.0, 5.0]
y1 = [144.19007,76.55647,37.58890,25.63092,21.23517]
y2 = [201.76977,108.34486,57.88546,34.82957,20.84889]

fig = pl.figure(figsize=(8,6), dpi=100, facecolor='white')

for i in range(len(x)):
	x[i] = x[i]/6.0
	y1[i] = y1[i]/240.0
	y2[i] = y2[i]/240.0
	
pl.xlim(0, 1)
pl.ylim(0, 1)

font = {'family' : 'serif',
		'color'  : 'black',
		'weight' : 'normal',
		'size'   : 16,
		}

ax = pl.gca()
ax.set_xticks(np.linspace(0, 1, 7))
ax.set_xticklabels(('0','1','2','5','10','20','(pipelines)'))
ax.set_yticks(np.linspace(0, 1, 7))
ax.set_yticklabels(('0','40.0','80.0','120.0','160.0','200.0','(s)'))
ax.set_xlabel('Number of Pipelines',fontdict=font)
ax.set_ylabel('Consumed Time of Whole System(s)',fontdict=font)

pl.plot(x, y1, 'bp-', linewidth=1, label=' 100-nodes')
pl.plot(x, y2, 'rs-', linewidth=1, label=' 200-nodes')
pl.legend(loc='best')
pl.grid(True)
pl.title('Time Consumed with 200MB Data')
pl.savefig('pipelines.png')
pl.show()
