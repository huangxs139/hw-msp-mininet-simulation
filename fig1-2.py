#!/usr/bin/python

import numpy as np
import pylab as pl

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
y1 = [0.00322,0.00689,0.01039,0.05430,0.21682,0.20085,1.28296,8.53060,18.04189,26.70554]
y2 = [0.08528,0.02885,0.06978,0.04796,0.23219,0.34078,1.42699,10.65824,16.34647,29.38161]
y3 = [0.03738,0.02734,0.05275,0.06592,0.18420,0.29384,1.92523,10.94366,19.81856,28.41096]
y4 = [0.04492,0.03231,0.05194,0.07596,0.17014,1.06216,9.11064,12.38036,20.69195,27.58815]
y5 = [0.00416,0.01261,0.01449,0.01909,0.02421,0.02738,0.04036,0.04613,0.05205,0.05800]
y6 = [0.01148,0.01062,0.01491,0.01241,0.02144,0.02324,0.03382,0.03773,0.04143,0.04510]
y7 = [0.00591,0.00660,0.00739,0.00608,0.00888,0.01442,0.01856,0.02349,0.03049,0.03380]
y8 = [0.00378,0.00287,0.00452,0.00366,0.00604,0.00673,0.00860,0.01074,0.01564,0.01919]

fig = pl.figure(figsize=(8,6), dpi=100, facecolor='white')

for i in range(0, 10):
	x[i] = x[i]/11.0
	y1[i] = (y1[i]+5.0)/50.0
	y2[i] = (y2[i]+5.0)/50.0
	y3[i] = (y3[i]+5.0)/50.0
	y4[i] = (y4[i]+5.0)/50.0
	y5[i] = (y5[i]+5.0)/50.0
	y6[i] = (y6[i]+5.0)/50.0
	y7[i] = (y7[i]+5.0)/50.0
	y8[i] = (y8[i]+5.0)/50.0
pl.xlim(0, 1)
pl.ylim(0, 1)

font = {'family' : 'serif',
		'color'  : 'black',
		'weight' : 'normal',
		'size'   : 16,
		}

ax = pl.gca()
ax.set_xticks(np.linspace(0, 1, 12))
ax.set_xticklabels(('0','1','2','4','8','16','32','64','128','256','512','(MB)'))
ax.set_yticks(np.linspace(0, 1, 11))
ax.set_yticklabels(('-5.00', '0','5.00','10.00','15.00','20.00','25.00','30.00','35.00','40.00','(s)'))
ax.set_xlabel('Size of Single File in X-Updating(MB)',fontdict=font)
ax.set_ylabel('Consumed Time of X-Delta(s)',fontdict=font)

pl.plot(x, y1, 'bp-',  linewidth=1, label='Total Time  Seq.Mod')
pl.plot(x, y2, 'cs-',  linewidth=1, label='Total Time  Seq.R/A')
pl.plot(x, y3, 'g^-',  linewidth=1, label='Total Time  Rand.Mod')
pl.plot(x, y4, 'kv-',  linewidth=1, label='Total Time  Rand.R/A')
pl.plot(x, y5, 'bp--', linewidth=1, label='  CPU Time  Seq.Mod')
pl.plot(x, y6, 'cs--', linewidth=1, label='  CPU Time  Seq.R/A')
pl.plot(x, y7, 'g^--', linewidth=1, label='  CPU Time  Rand.Mod')
pl.plot(x, y8, 'kv--', linewidth=1, label='  CPU Time  Rand.R/A')
pl.plot([0,1],[0.1,0.1], 'r', linewidth = 2);
pl.legend(loc='best')
pl.grid(True)
pl.title('Time Consuming')
pl.savefig('time-unzip.png')
pl.show()
