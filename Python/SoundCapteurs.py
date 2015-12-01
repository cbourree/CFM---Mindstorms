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
            self._voie_can = 0
            self._digi1 = 12
            self._digi2 = 16
        else:
            self._voie_can = 1
            self._cmd1 = 18
            self._cmd2 = 22
        GPIO.setup(self._digi1, GPIO.OUT)
        GPIO.setup(self._digi2, GPIO.OUT)

    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def getSon(self):
        GPIO.output(self._digi1, GPIO.HIGH)
        GPIO.output(self._digi2, GPIO.HIGH)
        tension = getTension(self._voie_can)
        GPIO.output(self._cmd, GPIO.LOW)
        return tension

    def BlancOuNoir(self):
        #1 Blanc, 2 Noir
        GPIO.output(self._cmd, GPIO.HIGH)
        time.sleep(0.2)
        tension = getTension(self._voie_can)
        GPIO.output(self._cmd, GPIO.LOW)
        if (tension < 2.6):
            return 1
        else:
            return 2
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nLuminosité ? {}\t" . format(self._port, self.isPressed())

