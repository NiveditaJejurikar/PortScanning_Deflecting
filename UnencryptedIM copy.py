'''
Nivu Jejurikar
Network Security - Daniel Votipka

This is an unencrypted peer to peer chat program that allows a server and client
to send messages to each other continuously. The user inputs the hostname to 
run the program, and an instance of either the client or server program is called 

'''
import argparse
import select
import socket
import sys
import signal
import select

#use mutually exclusive group so that usr may either choose 
#client or server mode, but not both. accept hostname as an argument
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--s", action = "store_true")
group.add_argument("--c", help = "enter client mode after server mode initiated")

args = parser.parse_args()

#call server code or client code depending on usr input
if args.s:
	import server
elif args.c:
	import client




