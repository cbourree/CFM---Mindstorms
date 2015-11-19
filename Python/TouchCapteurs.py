#!/usr/bin/python
#-*- coding: utf-8 -*-

import CAN
import RPi.GPIO as GPIO

class CapteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass
    
class TouchCapteur():

    _PORTS = "1234" #Liste des ports disponibles
    
    def __new__(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port
        if port == '1':
            self._entree = 0
        elif port == '2':
            self._entree = 1
        elif port == '3'
            self._entree = 2
        else:
            self._entree = 3
        GPIO.setup(pinA, GPIO.IN)
        GPIO.setup(pinB, GPIO.IN)
        return self

    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def isPressed(self):
        tension = CAN.getTension(self._entree)
        if tension < 2:
            return False
        else:
            return True
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nEtat presse ? {}\t" . format(self._port, self.isPressed())

