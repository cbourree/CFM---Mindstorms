#!/usr/bin/python
#-*- coding: utf-8 -*-

from CAN import getTension
import RPi.GPIO as GPIO
import time

class CapteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass
    
class SoundCapteur():

    _PORTS = "12" #Liste des ports disponibles
    
    def __init__(self, port):
        if port not in SoundCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port
        if port == '1':
            self._voie_can = 2
            self._digi1 = 12
            self._digi2 = 16
        else:
            self._voie_can = 3
            self._digi1 = 18
            self._digi2 = 22
        GPIO.setup(self._digi1, GPIO.OUT)
        GPIO.setup(self._digi2, GPIO.OUT)

    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def getSon(self):
        #return en % la puissance sonore reçue par le capteur
        GPIO.output(self._digi1, GPIO.HIGH)
        GPIO.output(self._digi2, GPIO.HIGH)
        tension = getTension(self._voie_can)
        GPIO.output(self._digi1, GPIO.LOW)
        GPIO.output(self._digi2, GPIO.LOW)
        return tension * 20
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nSon : {}\t" . format(self._port, self.getSon())

