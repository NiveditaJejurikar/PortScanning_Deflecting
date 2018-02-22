import socket
import argparse 
from datetime import datetime
from random import shuffle
import time
global s
global serv

parser = argparse.ArgumentParser()
parser.add_argument("FOOBAR", help = "enter the hostname or IP address of the machine that is to be scanned")

args = parser.parse_args()

#save the inputted IP address in target IP variable
targetIP = args.FOOBAR



totalOpen = 0

range = [x for x in range(0, 65535)]
#shuffle the ports so that the program does not scan in numerical order
#that way the port scanner may go undetected 
shuffle(range)

start = time.clock()

for i in range:
	#for each port check the connection
	#obtain service type and store port no and service type in a file
	
	#serv = socket(targetIP, [protocolname])
	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = s.connect_ex((targetIP, i))
		
		try:
			serv = socket.getservbyport(i, "tcp")
		except:
			serv = 'NA'

		if (result == 0):
			print ('%d' % (i,) + ' (' + serv + ') was open')
			f = open("scanner.txt", "w+")
			f.write('%d' % (i,) + ' (' + serv + ') was open')
			totalOpen+=1


		#close the file and the socket object when finished
		#then compute time elapsed and scan rate

	except:
		continue
end = time.clock()

time_elapsed = end - start
scan_rate = 65535/time_elapsed
print("time elapsed = " + str(time_elapsed))
print("total open ports = " + str(totalOpen))
print("time per scan = " + str(scan_rate))
