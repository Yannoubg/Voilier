#!/usr/bin/python
import socket
IP_Dest="192.168.0.221"
PORT = 5005
#ligne creation trame
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("Tchuss",(IP_Dest,PORT))
