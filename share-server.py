#! usr/bin/python3

import socket
import struct as st

MAX = 212992

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
print('127.0.0.1:65432')
file = b''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            chuncks = st.unpack('i', conn.recv(32))[0]
            for chuck in range(chuncks):
                bytes = st.unpack('i', conn.recv(32))[0] % MAX
                file += conn.recv(bytes)
            break
            
with open('Store.bin', 'wb') as co:
    co.write(file)
