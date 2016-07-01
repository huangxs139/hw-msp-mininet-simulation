#!/usr/bin/python

import os
#filePath = '/home/tcoops/results/'
#ansPath = '/home/tcoops/analysis/'
#filePath = '/home/hxs139/mntest/results/'
#ansPath = '/home/hxs139/mntest/analysis/'
filePath = '/home/zyz915/hxs/mntest/results/'
ansPath = '/home/zyz915/hxs/mntest/analysis/'

def handler(n = 10, m = 3, s = 1): 
	files = os.listdir(filePath)
	ans = []
	for eachFile in files:
		f = open(filePath + eachFile, 'r')
		lines = f.readlines()
		label, src, dest = 0, 0, 0
		flag = False
		for line in lines:
			if 'local' in line:
				flag = True
				p1 = line.find('local') 
				p2 = line.find('port', p1)
				ip = line[p1+6 : p2-1]
				dest = int(ip.split('.')[3])
				
				p3 = line.find('with')
				p4 = line.find('port', p3)	
				ip = line[p3+5 :  p4-1]
		    		src = int(ip.split('.')[3])	

			        print src, dest
				if src == s and dest > n:
					label = 3
 			
				elif dest == src + 1 or (src == n and dest == 1):
					label = 1
				elif src == dest + 1 or (src == 1 and dest == n):
					label = 2
				
				
			if '/sec' in line:
				parts = line.split()
				bw = float(parts[-2])
		if flag: ans.append([dest, label, bw])
	f.close()
	return ans
				
if __name__ == '__main__':
	ans = handler()
	print ans
	f = open(ansPath + 'ans', 'w')
	#line = 'id' + ' '*10 + 'label' + ' '*10 + 'bw'
	line = ''
	for each in ans:
		tmp = str(each[0]) + ' ' + str(each[1])  + ' ' + str(each[2]) 
		line +=  tmp + '\n'

	
	f.write(line)
	f.close()
