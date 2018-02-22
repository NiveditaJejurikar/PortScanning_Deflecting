import argparse
import select
import socket
import sys
import signal
import select

#set up the socket to accept the address domain of the socket, 
#and to accept characters to be read in a continuous flow
global serverSocket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ""
port = 9999

null = ""

serverSocket.bind((host, port))

#This program is set up to listen to up to 5 clients
#accept the connection using the socket object and address inputted
serverSocket.listen(5)

serverSocket, addr = serverSocket.accept()


def handler(signum, frame):
	clientSocket.close()
	sys.exit(0)

signal.signal(signal.SIGINT, handler)

#use select method to either read in continous messages from the command
#line, or from the server in a loop. Display output on the screen 
while True:
	read_list = [serverSocket, sys.stdin]
	read_socket, write_socket, error_socket = select.select(read_list, [], [])

	for sock in read_socket:
		if sock == serverSocket:
			message = serverSocket.recv(2048)
			sys.stdout.write(message)
			sys.stdout.flush()
			if message == null:
				serverSocket.close()
				break

		elif sock == sys.stdin:
			msg = sys.stdin.readline()
			print(msg)
			serverSocket.send(msg)
			sys.stdout.flush()

		else:
			print("NOT std input or serversocket\n")



