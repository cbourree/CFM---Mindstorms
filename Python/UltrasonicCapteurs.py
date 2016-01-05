#!/usr/bin/python
#-*- coding: utf-8 -*-

from smbus import SMBus
import time

class CapteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass

    
class UltrasonicCapteur():

    _PORTS = "34" #Liste des ports disponibles
    
    def __init__(self, port):
        if port not in UltrasonicCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port
        if port == '3':
            self._read_addr = 2
            self._write_addr = 3
        else:
            self._read_addr = 2
            self._write_addr = 3
        self._bus = SMBus(1)
 
    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def getInfos(self):
        pass

    def setScaleFactor(self, value):
        self._bus.write_byte_data(self._write_addr, 0x51, value)
        time.sleep(0.1)
        
    def setScaleDivisor(self, value):
        self._bus.write_byte_data(self._write_addr, 0x52, value)
        time.sleep(0.1)

    def setActualZero(self, value):
        self._bus.write_byte_data(self._write_addr, 0x50, value)
        time.sleep(0.1)

    def setInterval(self, value):
        self._bus.write_byte_data(self._write_addr, 0x40, value)
        time.sleep(0.1)

    def getInterval(self):
        data = self._bus.read_i2c_block_data(self._read_addr, 0x40, 1)
        time.sleep(0.1)
        return data[0]

        
    def getDistance(self):
        #Retourne la distance devant le capteur.
        #self._bus.write_byte_data(self._write_addr, 0x41, 0x01)
        time.sleep(0.1)
        data = self._bus.read_i2c_block_data(self._read_addr, 0x42, 8)
        distance = (data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6] + data[7]) / 8
        return distance

    
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nVersion : V1.0\nID produit : LEGO\nDistance : {}\t" . format(self._port, self.getDistance())

UC = UltrasonicCapteur('3')
UC._bus.read_byte(2)
