from __future__ import division 
import spidev 


class EntreeExistErreur(Exception):
    #L'entrée n'existe pas
    pass

def lire_analog(entree_analog = 0):
    liaison = spidev.SpiDev(0, 0) #Créée liaison SPI sur le port 0, adresse 0
    liaison.max_speed_hz = 300000 # en Hertz 

    # Initialisation des parametres de lecture
    if entree_analog >= 0 and entree_analog <= 7: #Choie de la voie a convertir
        msb_addr_voie = 128 + 8 * entree_analog # msb_addr = (entree_analog + 8) << 4
    else:
        raise EntreeExistErreur
    to_send = [msb_addr_voie, 0]
    #to_send = [msb_addr_voie, ] A tester

    # Lecture 
    rd_octets = liaison.xfer2(to_send) 

    # La reponse arrive sur deux octets 
    msb = rd_octets[0] 
    lsb = rd_octets[1] 
    value = (msb << 8) + lsb # inclu dans  [0, 1024]
    
    calcul = 2 * (value * 5) / 1024.0
    return calcul 

while 1:
    print(lire_analog(7))

