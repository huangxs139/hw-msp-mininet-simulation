#!/usr/bin/python

import numpy as np
import pylab as pl

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
y1 = [0.19539547,0.195375919,0.195366144,0.195361614,0.195360839,0.195360065,0.195359677,0.195359826,0.195359852,0.195359889]
y2 = [0.195384026,0.195367813,0.195359468,0.195356488,0.195355833,0.19535473,0.195354521,0.195354849,0.195354879,0.195354832]
y3 = [0.197756767,0.197794914,0.197713614,0.1972574,0.196333528,0.195871443,0.195640519,0.195525236,0.195467617,0.195438679]
y4 = [0.196862221,0.19687891,0.19682622,0.196541548,0.195960641,0.195669591,0.195524216,0.195451915,0.195415713,0.195397459]

fig = pl.figure(figsize=(8,6), dpi=100, facecolor='white')

for i in range(0, 10):
	x[i] = x[i]/11.0
	y1[i] = y1[i]/0.8
	y2[i] = y2[i]/0.8
	y3[i] = y3[i]/0.8
	y4[i] = y4[i]/0.8
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
ax.set_yticks(np.linspace(0, 1, 5))
ax.set_yticklabels(('0','20.00','40.00','60.00','(%)'))
ax.set_xlabel('Size of Single File in X-Deltaing(MB)',fontdict=font)
ax.set_ylabel('Delta-size/Original-size as Delting Rate(%)',fontdict=font)

pl.plot(x, y1, 'bp-', linewidth=1, label='Seq.Mod')
pl.plot(x, y2, 'rs-', linewidth=1, label='Seq.R/A')
pl.plot(x, y3, 'g^-', linewidth=1, label='Rand.Mod')
pl.plot(x, y4, 'cv-', linewidth=1, label='Rand.R/A')
pl.legend(loc='best')
pl.grid(True)
pl.title('Delting Rate')
pl.savefig('rate.png')
pl.show()

