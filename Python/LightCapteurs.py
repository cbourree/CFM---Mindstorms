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
        if port not in LightCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port
        if port == '1':
            self._voie_can = 2
            self._cmd = 12
        else:
            self._voie_can = 3
            self._cmd = 18
        GPIO.setup(self._cmd, GPIO.OUT)
        self._valeur_limite = 2.6

    def getPort(self):
        return self._port

    def setPort(self, port):
        if port not in TouchCapteur._PORTS:
            raise CapteurPortErreur
        self._port = port

    def getLuminosite(self):
        #return la tension mesuré en sortie du capteur
        GPIO.output(self._cmd, GPIO.HIGH)
        time.sleep(0.2)
        tension = getTension(self._voie_can)
        GPIO.output(self._cmd, GPIO.LOW)
        return tension

    def BlancOuNoir(self):
        # return 1 si Blanc, 2 si Noir
        GPIO.output(self._cmd, GPIO.HIGH)
        time.sleep(0.2)
        tension = getTension(self._voie_can)
        GPIO.output(self._cmd, GPIO.LOW)
        if (tension < self._valeur_limite):
            return 1
        else:
            return 2

    def etalonnage(self, valeur_limite = -1):
        #Pour changer la valeur limite entre "Blanc" et "Noir"
        if valeur_limite == -1:
            #Etalonage auto
            pass
        else:
            self._valeur_limite = valeur_limite
    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Capteur sur le port {}\nLuminosité ? {}\t" . format(self._port, self.isPressed())

