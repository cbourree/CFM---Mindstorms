from __future__ import division 
import spidev 
 
def lire_analog(puce_spi = 0, entree_analog = 1): 
    liaison = spidev.SpiDev(0, puce_spi) 
    liaison.max_speed_hz = 300000 # en Hertz 

    # Initialisation des parametres de lecture
    # (cf datasheet pour les curieux) 
    if entree_analog == 0: 
        value = 128 
    else: 
        value = 160 
    to_send = [value, 0] 

    # Lecture 
    rd_octets = liaison.xfer2(to_send) 

    # La reponse arrive sur deux octets 
    msb = rd_octets[0] 
    lsb = rd_octets[1] 
    value = (msb << 8) + lsb 
    calcul = 2 * (value * 3.3) / 1024.0 
    return calcul 

print(lire_analog())

if __name__ == '__main__': 
    print(lire_analog())
