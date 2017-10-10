#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP_Dest = "192.168.0.221" #Addresse du serveur
port = 8888 #Port du serveur
trame = bytearray([22,2,30,90])

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_DGRAM = Internet
#socket.SOCK_STREAM = UDP

print 'Connexion réussi sur le serveur...'

print 'Addresse de destination: ',IP_Dest

print 'Port de destination: ',port

print 'Message envoyé: ', trame[0],trame[1],trame[2],trame[3]

connexion_serveur.sendto (trame, (IP_Dest, port)) #Envoie du message au serveur

data, addresse = connexion_serveur.recvfrom(4)

print '------------------------'

print 'Réponse du serveur:'

print 'ID: ', ord(data[0])
print 'Taille: ', ord(data[1])
print 'Safran: ',ord(data[2])
print 'GV: ',ord(data[2])
