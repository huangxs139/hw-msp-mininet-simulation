#!/usr/bin/python

import numpy as np
import pylab as pl

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
y1 = [0.05850,0.12621,0.30241,0.89143,2.01464,4.13082,9.25237,19.49590,28.98714,39.87817]
y2 = [0.13571,0.30996,0.45205,0.88080,1.54716,3.57273,9.60639,18.74649,29.44677,40.46399]
y3 = [0.26609,0.28867,0.52844,0.85761,1.72029,4.23737,9.65794,16.49456,28.50116,39.09802]
y4 = [0.18193,0.26259,0.46527,0.62116,1.72876,3.22231,8.82679,16.69567,26.01210,33.79677]
y5 = [0.01286,0.01404,0.01451,0.01420,0.01771,0.02397,0.03023,0.03527,0.04085,0.04929]
y6 = [0.00538,0.00614,0.00743,0.00855,0.01205,0.01938,0.00789,0.02662,0.03319,0.03948]
y7 = [0.00331,0.00302,0.00614,0.01139,0.00844,0.00483,0.01293,0.01969,0.02527,0.03137]
y8 = [0.00075,0.00052,0.00050,0.00123,0.00280,0.00610,0.00773,0.01252,0.01784,0.02425]

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
ax.set_xlabel('Size of Single File in X-Deltaing(MB)',fontdict=font)
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
pl.savefig('time-zip.png')
pl.show()
