#!/usr/bin/python
import socket
IP_Serv="127.0.0.1" "192.168.X.1"
PORT=8888
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_Serv,PORT))
while True :
    data, addr=sock.recvfrom(6)
    print data
