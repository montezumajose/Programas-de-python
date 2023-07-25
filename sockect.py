#!/usr/bin/python3
import socket

port = int(input("Introduzca el puerto a escuchar: "))
size = 512
host = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(5)
print('Listening in port '+str(port))
connection, client_addr = sock.accept()
data = connection.recv(size)
if data:
    print("connection from: ", client_addr)
sock.close()