#!/usr/bin/python
#-*- coding: utf-8 -*-

from CAN import getTension
import RPi.GPIO as GPIO
import time

class CapteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass
    
class LightCapteur():

    _PORTS = "12" #Liste des ports disponibles
    
    def __init__(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port
        if port == '1':
            self._voie_can = 0
            self._cmd = 12
        else:
            self._voie_can = 1
            self._cmd = 18
        GPIO.setup(self._cmd, GPIO.OUT)

    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def getLuminosite(self):
        GPIO.output(self._cmd, GPIO.HIGH)
        tension = getTension(self._voie_can)
        print(tension)
        GPIO.output(self._cmd, GPIO.LOW)
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nLuminosité ? {}\t" . format(self._port, self.isPressed())

