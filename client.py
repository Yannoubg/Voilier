#!/usr/bin/python
import socket
IP="127.0.0.1"
PORT = 8888
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("Salut",(IP,PORT))
