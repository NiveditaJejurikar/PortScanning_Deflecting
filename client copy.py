import argparse
import select
import socket
import sys
import signal
import select

global clientSocket

#set up socket object and establish connection with server 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
clientSocket.connect((host, 9999))

null = ""

def handler(signum, frame):
	clientSocket.close()
	sys.exit(0)

signal.signal(signal.SIGINT, handler)

#use select method to either read in continous messages from the command
#line, or from the server. Display output on the screen 
while True:
	read_list = [sys.stdin, clientSocket]
	read_socket, write_socket, error_socket = select.select(read_list, [], [])
	for socks in read_socket:
		if socks == clientSocket:
			message = clientSocket.recv(2048)
			sys.stdout.write(message)
			sys.stdout.flush()

			if message == null:
				clientSocket.close()
				break


		elif socks == sys.stdin:
			user_message = sys.stdin.readline()
			clientSocket.send(user_message)
			sys.stdout.flush()

		else:
			print("NOT std input or serversocket\n")





