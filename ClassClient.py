#!/usr/bin/env python
# -*-coding:Latin-1 -*
# _*_ coding: utf-8 _*_

import codecs
import socket

class VoilierClient:
	def __init__(self):
		self.ipserv=""
		self.port=0
		self.valSF=0
		self.valGV=0
		self.idtrame=0
		self.VitVent=0
		self.DirVent=0
		self.Gite=0
		self.latitude=0
		self.longitude=0

	def initcom(self,ip,port):
		self.ipserv=ip
		self.port=port
		self.sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



	def txrx(self):
		trame = bytearray([self.idtrame,2,self.valSF,self.valGV])
		self.sock.sendto (trame, (self.ipserv, self.port)) #Envoie du message au serveur

		data, addresse = self.sock.recvfrom(1024)

		self.idtrame=data[0]
		self.VitVent=data[2]
		self.DirVent=data[3]
		self.Gite=data[4]

		lat0=((ord(data[5])<<24))
		lat1=((ord(data[6])<<16))
		lat2=((ord(data[7])<<8))
		lat3=((ord(data[8])<<0))

		lat=lat0|lat1|lat2|lat3

		if lat3 > 127:
			lat=(~lat)&0xFFFFFFFF
			lat=lat+1
			lat=lat*-1

		self.latitude=float(lat)/10000000

		lon0=((ord(data[9])<<24))
		lon1=((ord(data[10])<<16))
		lon2=((ord(data[11])<<8))
		lon3=((ord(data[12])<<0))

		lon=lon0|lon1|lon2|lon3

		if lon3 > 127:
			lon=(~lon)&0xFFFFFFFF
			lon=lon+1
			lon=lon*-1
	

		self.longitude=float(lon)/10000000
