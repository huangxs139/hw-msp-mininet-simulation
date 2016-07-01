#!/usr/bin/python

import numpy as np
import pylab as pl

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
y1 = [13.90333,29.07269,43.07126,54.81747,73.37745,87.63757,96.26271,116.16400,124.74244,144.19007]
y2 = [7.61853,18.92751,22.39993,29.92249,37.94524,44.99881,52.90031,62.60326,68.25882,76.55647]
y3 = [4.18810,7.95977,11.51180,15.14215,23.58828,22.38974,26.84780,30.26653,34.08719,37.58890]
y4 = [5.67531,6.24385,8.44265,10.89099,13.69206,15.55893,22.76216,20.22317,28.17699,25.63092]
y5 = [5.61250,8.03934,7.88384,10.03011,14.43571,13.50460,15.52813,17.14787,19.00744,21.23517]

fig = pl.figure(figsize=(8,6), dpi=100, facecolor='white')

for i in range(len(x)):
	x[i] = x[i]/11.0
	y1[i] = y1[i]/165.0
	y2[i] = y2[i]/165.0
	y3[i] = y3[i]/165.0
	y4[i] = y4[i]/165.0
	y5[i] = y5[i]/165.0
	
pl.xlim(0, 1)
pl.ylim(0, 1)

font = {'family' : 'serif',
		'color'  : 'black',
		'weight' : 'normal',
		'size'   : 16,
		}

ax = pl.gca()
ax.set_xticks(np.linspace(0, 1, 12))
ax.set_xticklabels(('0','20','40','60','80','100','120','140','160','180','200','(MB)'))
ax.set_yticks(np.linspace(0, 1, 12))
ax.set_yticklabels(('0','15.0','30.0','45.0','60.0','75.0','90.0','105.0','120.0','135.0','150.0','(s)'))
ax.set_xlabel('Size of Transfered Data',fontdict=font)
ax.set_ylabel('Consumed Time of Whole System(s)',fontdict=font)

pl.plot(x, y1, 'bp-', linewidth=1, label=' 1-pipeline')
pl.plot(x, y2, 'rs-', linewidth=1, label=' 2-pipelines')
pl.plot(x, y3, 'g^-', linewidth=1, label=' 5-pipelines')
pl.plot(x, y4, 'kv-', linewidth=1, label='10-pipelines')
pl.plot(x, y5, 'ch-', linewidth=1, label='20-pipelines')
pl.legend(loc='best')
pl.grid(True)
pl.title('Time Consumed with 100-Nodes Under Each Switch')
pl.savefig('time_net.png')
pl.show()
