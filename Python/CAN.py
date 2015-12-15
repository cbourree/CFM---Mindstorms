#!/usr/bin/python
#-*- coding: utf-8 -*-

#Charger le SPI au démarrage de la RPI
#sudo raspi-config -> Advanced option -> SPI -> Ok -> OK
#Pour installer les libs nécéssaires
#sudo apt-get install python2.7-dev
#sudo apt-get install python3-dev
#sudo apt-get libevent-dev
#sudo pip install spidev
#Pour que ça fonctionne aussi en python 3.0
#sudo apt-get install python2.7-dev
#sudo apt-get install python3-dev
#sudo apt-get libevent-dev
#sudo pip3.0 install spidev

from __future__ import division 
import spidev 
import time

class EntreeExistErreur(Exception):
    #L'entrée n'existe pas
    pass

# Return la tension à l'entrée entree_analog du CAN MCP3008
# Tension comprise entre 0 et 5V
# Lève l'exception EntreeExistErreur si celle ci n'est pas comprise dans [0;7]
def getTension(entree_analog = 0):
    liaison = spidev.SpiDev(0, 0) #Créée liaison SPI sur le port 0, adresse 0
    liaison.max_speed_hz = 300000 # en Hertz 

    # Initialisation des parametres de lecture
    if entree_analog >= 0 and entree_analog <= 7: #Choie de la voie a convertir
        msb_addr_voie = 128 + 8 * entree_analog # On met nos donées su le msb
    else:
        raise EntreeExistErreur
    to_send = [msb_addr_voie, 0]

    #Lecture 
    rd_octets = liaison.xfer2(to_send) 

    #La reponse arrive sur deux octets 
    msb = rd_octets[0] 
    lsb = rd_octets[1] 
    value = (msb << 8) + lsb # inclu dans  [0, 1024]
    
    calcul = 2 * (value * 5) / 1024.0 # 5 pour 5V et 1024 car CAN 10 bits
    return calcul 

