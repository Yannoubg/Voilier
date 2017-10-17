#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

#IP_Dest = "192.168.0.221" #Addresse du serveur
IP_Dest = "127.0.0.1" #Addresse du serveur
port = 8888 #Port du serveur
idTrame=22
lgData=2
safran=30
gV=90
trame = bytearray([idTrame,lgData,safran,gV])


connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_DGRAM = Internet
#socket.SOCK_STREAM = UDP

print 'Connexion réussi sur le serveur...'

print 'Addresse de destination: ',IP_Dest

print 'Port de destination: ',port

print 'Message envoyé: ', trame[0],trame[1],trame[2],trame[3]

connexion_serveur.sendto (trame, (IP_Dest, port)) #Envoie du message au serveur

data, addresse = connexion_serveur.recvfrom(1024)


lat0=((ord(data[5])<<24))
lat1=((ord(data[6])<<16))
lat2=((ord(data[7])<<8))
lat3=((ord(data[8])<<0))

if lat3 > 127:
	latitude=(~latitude)&0xFFFFFFFF
	latitude=latitude+1
	latitude=latitude*-1

lat=lat0|lat1|lat2|lat3

lon0=((ord(data[9])<<24))
lon1=((ord(data[10])<<16))
lon2=((ord(data[11])<<8))
lon3=((ord(data[12])<<0))

if lon3 > 127:
	longitude=(~longitude)&0xFFFFFFFF
	longitude=longitude+1
	longitude=longitude*-1

lon=lon0|lon1|lon2|lon3


print '------------------------'

print 'Réponse du serveur:'

print 'ID: ', ord(data[0])
print 'Taille: ', ord(data[1]),' octets'
print 'vitVent: ', ord(data[2])
print 'dirVent: ', ord(data[3])
print 'lattitude: ', ord(data[5]), ord(data[6]), ord(data[7]), ord(data[8])
print 'latitude.hex', hex(ord(data[5])),hex(ord(data[6])),hex(ord(data[7])),hex(ord(data[8]))
print 'latitude ', lat
print 'longitude: ',lon
print 'gite: ',ord(data[4])
