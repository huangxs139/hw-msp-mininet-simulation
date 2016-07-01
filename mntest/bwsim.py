#!/usr/bin/python

import re, os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.link import TCLink, Intf
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.log import lg, info, error, output

linkopts = dict(bw=1000)
#linkopts = dict()
sw_list = []
status, neib, ip = {}, {}, {}

class myParam:
	"using for pass major params"
	def __init__(self, **params):
		"n -- nodes per switch, m -- switches in first layer\
		 data_size -- size of transfered data, pipes -- number of pipelines"
		self.n = (100 if 'n' not in params else params['n'])
		self.m = (5 if 'm' not in params else params['m'])
		self.data_size = (20 if 'data_size' not in params else params['data_size'])
		self.pipes = (1 if 'pipes' not in params else params['pipes'])

	def show(self):
		print self.n, self.m, self.data_size, self.pipes

class myTopo( Topo ):
	"One root switch, m sub-switches, n hosts under 1st sub-switch, 1 host under other sub-switches"
	def build( self, n=3, m=2 ):
		sw_list.append(self.addSwitch('s0'))
		for i in range(m):
			sw_list.append(self.addSwitch('s%d' % (i+1)))
			self.addLink(sw_list[0], sw_list[i+1], **linkopts)
		for i in range(n):
			hs = self.addHost('h%d' % (i+1))
			self.addLink(sw_list[1], hs, **linkopts)
		for i in range(n+1, n+m):
			hs = self.addHost('h%d' % i)
			self.addLink(sw_list[i-n+1], hs, **linkopts)

		#neib['h1'] = ['h2', 'h%d'%n]	#nodes in TCP circle come the first
		neib['h1'] = []					#line for circle-last
		for i in range(n+1, n+m):
			neib['h1'].append('h%d'%i)	#nodes across root switches come the second
			neib['h%d'%i] = ['h1']
		neib['h1'].append('h2')		#line for circle-last
		neib['h1'].append('h%d'%n)		#line for circle-last
		neib['h%d'%n] = ['h%d'%(n-1), 'h1']
		for i in range(2, n):
			neib['h%d'%i] = ['h%d'%(i-1), 'h%d'%(i+1)]

def perNodeProc((h, prm)):
	'''while status[h.name] != 2:
		continue
	for hs in neib[h.name]:
		if status[hs] == 0:
			status[hs] = 1
			h.cmdPrint('iperf -c %s -N -n %d -f M' % (ip[hs], data_size*1024*1024))
			#print '%s iperf -c %s -N -n %s' % (h.name, ip[hs], '2147483648')
			#h.cmd('sleep 5')
			res = h.waitOutput()
			status[hs] = 2
	'''
	perd = prm.data_size / prm.pipes
	flag = 0
	while flag == 0:
		flag = 1
		for i in range(prm.pipes):
			for hs in neib[h.name]:
				if status[hs][i] == 0:
					flag = 0
					if status[h.name][i] == 2:
						status[hs][i] = 1
						h.cmdPrint('iperf -c %s -N -n %d -f M' % (ip[hs], perd*1024*1024))
						#print '%s iperf -c %s -N -n %s' % (h.name, ip[hs], perd*1024*1024)
						res = h.waitOutput()
						status[hs][i] = 2

def simTrans(hosts, prm):
	fname = str(prm.n) + 'nodes.' + str(prm.data_size) + 'MB.' + str(prm.pipes) + 'pipes.out'
	for h in hosts:
		full_name = "results/%04d/%s"%(int(h.name.split('h')[1]), fname)
		os.system("rm %s" % full_name)
		status[h.name] = [0 for i in range(prm.pipes)]
		ip[h.name] = h.IP()
		h.cmdPrint('iperf -s -f M >> %s &'%full_name)
	'''for h1 in hosts:
		for h2 in hosts:
			if h1 == h2:
				continue
			print "Testing %s and %s after running server" % (h1.name, h2.name)
			net.iperf( (h1, h2) )
	'''
	print neib
	status['h1'] = [2 for i in range(prm.pipes)]	#start node
	print status
	k = []
	for h in hosts:
		k.append((h, prm))
	pool = ThreadPool(50)
	pool.map(perNodeProc, k)
	pool.close()
	pool.join()

	for h in hosts:
		h.cmdPrint('kill %iperf')

def perfTest():
	"Create network and run simple performance test"

	prm = myParam(n=200, data_size=200)
	print prm.n, prm.m, prm.data_size, prm.pipes
	topo = myTopo(prm.n, prm.m)
	net = Mininet(topo=topo, link=TCLink)

	net.start()
	print "Dumping host connections"
	dumpNodeConnections( net.hosts )
	print "Dumping switch connections"
	dumpNodeConnections( net.switches )
	#print "Testing network connectivity"
	#net.pingAll()
	print "Testing bandwidth under s1"
	h1, h2 = net.get('h1', 'h2')
	net.iperf((h1, h2))
	print "Testing bandwidth across tree"
	h1, h2 = net.get('h1', 'h%d'%(prm.n+1))
	net.iperf((h1, h2))

	for p in (1, 2, 5, 10, 20):
		prm.pipes = p
		simTrans(net.hosts, prm)
	#CLI( net )
	net.stop()

if __name__ == "__main__":
	lg.setLogLevel('info')
	perfTest()
