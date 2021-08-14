#!/usr/bin python3

import socket

MAX = 212992

HOST = input("Server ip: ")  # The server's hostname or IP address
PORT = int(input("Server port: "))        # The port used by the server

with open(input('file :'), 'rb') as co:
	file = list(co.read())
	bytes = len(file)
	chuncks = bytes // (MAX)
	chunck = [file[i*MAX:(i+1)*MAX] for i in range(chuncks)] + [file[chuncks*MAX:]]

if chunks > MAX:
	exit()
	
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(st.pack('i', chunks))
	for chnk in chunck:
		s.sendall(st.pack('i',len(chnk)))
		s.sendall(chnk)

