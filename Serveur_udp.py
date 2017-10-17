#!/usr/bin/env python
# -*-coding:Latin-1 -*
# _*_ coding: utf-8 _*_

import codecs
import socket

#IP_Serv = "192.168.0.221" #IP Raspi
IP_Serv = "127.0.0.1"
port = 8888

ID = 65
TAILLE = 5
VVENT = 50
DVENT = 128
GITE = 12

sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind ((IP_Serv, port))

while True:
    print "_______________________________________________________"
    data,addr = sock.recvfrom (1024) #ligne de décodage des trames.
    print "ID du systeme", ord (data[0])
    print "Taille de la trame", ord (data[1])
    print "Position de la GV", ord (data[2])
    print "Position du safran", ord (data[3])

    lat1 = 1651782
    lon1 = 210122287
    #lat2 = 52.406374
    #lon2 = 16.9251681

    b3=(lat1>>24)
    b2=(lat1>>16)&0xFF
    b1=(lat1>>8)&0xFF
    b0=(lat1>>0)&0xFF

    b4=(lon1>>24)
    b5=(lon1>>16)&0xFF
    b6=(lon1>>8)&0xFF
    b7=(lon1>>0)&0xFF

    print ""
    print ""
    print "latittude", lat1
    print " Valeur Hexa de b3 : ", hex(b3) 
    print " Valeur Hexa de b2 : ", hex(b2)
    print " Valeur Hexa de b1 : ", hex(b1)
    print " Valeur Hexa de bo : ", hex(b0)

    trame_reponse = bytearray([ID, TAILLE, VVENT, DVENT, GITE, b3,b2,b1,b0,b4,b5,b6,b7]) #bytearray creer un tableau.
            
    sock.sendto(trame_reponse, addr)






