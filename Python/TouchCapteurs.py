#!/usr/bin/python
#-*- coding: utf-8 -*-

from CAN import getTension
import RPi.GPIO as GPIO
import time

class CapteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass

class TouchCapteur():

    _PORTS = "1234" #Liste des ports disponibles
    
    def __init__(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port
        if port == '1':
            self._voie_can = 2
        elif port == '2':
            self._voie_can = 3
        elif port == '3':
            self._voie_can = 0
        else:
            self._voie_can = 1

    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def isPressed(self):
        #Return True si le bouton du capteur est pressé, False sinon
        tension = getTension(self._voie_can)
        if tension > 2:
            return True
        else:
            return False

    def waitIsPressed(self):
        #Met en pause le programme jusqu'à que le capteur soit pressé
        while (self.isPressed() != 1):
            time.sleep(0.1)
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nEtat presse ? {}\t" . format(self._port, self.isPressed())

