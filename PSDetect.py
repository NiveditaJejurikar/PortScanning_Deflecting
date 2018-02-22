
import dpkt
import pcapy
import pcap
import socket
import time
import datetime
import sys
import struct
import binascii
import socket
import textwrap
import getopt
from struct import *

#set the filter here to lo0
pc = pcap.pcap(name = "lo0", immediate = True)


scanCount = {}
lastPort = {}
start = {}
end = {}
timeScanned = {}
scannerFound = {}

decode = {pcap.DLT_LOOP:dpkt.loopback.Loopback,
		pcap.DLT_NULL:dpkt.loopback.Loopback,
		pcap.DLT_EN10MB:dpkt.ethernet.Ethernet }[pc.datalink()]

for ts, pkt in pc:
	packet = `decode(pkt)`

	eth = dpkt.loopback.Loopback(pkt)
	if isinstance(eth.data, dpkt.ip.IP):
		IPsource = eth.data.src  
		TCP_PORT = eth.data.data.dport

	if IPsource in scanCount:
		expport = lastPort[IPsource] + 1
		if TCP_PORT == expport: 
			lastPort[IPsource] += 1
			scanCount[IPsource]+=1
			timeScanned[scanCount[IPsource]] = time.clock()
			if scanCount[IPsource] >= 15:
				end = timeScanned[scanCount[IPsource]]
				before = scanCount[IPsource] - 14
				start = timeScanned[before]
				timeToScan = end-start
				if timeToScan < 5:
					print("Scanner detected. The scanner originated from host " + socket.inet_ntoa(IPsource))
					f = open("detector.txt", "w+")
					f.write("Scanner detected. The scanner originated from host " + socket.inet_ntoa(IPsource))
				f.close()
		else:
			scanCount[IPsource] = 1
			lastPort[IPsource] = TCP_PORT
			timeScanned[scanCount[IPsource]] = time.clock()
	else:
		scanCount[IPsource] = 1
		lastPort[IPsource] = TCP_PORT
		scannerFound[IPsource] = False
		timeScanned[scanCount[IPsource]] = time.clock()


