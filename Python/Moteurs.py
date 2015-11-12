#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

class MoteurExistErreur(Exception):
    #Un moteur est déjà initialisé sur ce port
    pass

class MoteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass

class MoteurConsigneErreur(Exception):
    #La consigne n'est pas comprises entre -100 et 100
    pass

class MoteurTempsErreur(Exception):
    #Le temps n'est pas possible
    pass
 
class Moteur():
 
    _MOTEURS = {} #Liste des ports utilisé
    _PORTS = "ABC" #Liste des ports disponibles
    _isRuning = False
    
    def __new__(cls, port, consigne = 0):
        if port in cls._MOTEURS: #Si le port est déjà pris
            raise MoteurExistErreur
        if port not in Moteur._PORTS:
            raise MoteurPortErreur
        if consigne < -100 or consigne > 100:
            raise MoteurConsigneError
        self = object.__new__(cls)
        self._port = port
        self._consigne = consigne
        cls._MOTEURS[port] = self
        if port == 'A':
            GPIO.setup(33, GPIO.OUT)
            GPIO.setup(35, GPIO.OUT)
            self._pwm1 = GPIO.PWM(33, 2000) #Fréquence 2000
            self._pwm2 = GPIO.PWM(35, 2000)
        elif port == 'B':
            GPIO.setup(37, GPIO.OUT)
            GPIO.setup(40, GPIO.OUT)
            self._pwm1 = GPIO.PWM(37, 2000)
            self._pwm2 = GPIO.PWM(40, 2000)
        else:
            GPIO.setup(38, GPIO.OUT)
            GPIO.setup(36, GPIO.OUT)
            self._pwm1 = GPIO.PWM(38, 2000)
            self._pwm2 = GPIO.PWM(36, 2000)
        return self

    def getPort(self):
        return self._port
    
    def getConsigne(self):
        return self._consigne

    def isRuning(self):
        return self._isRuning

    def setPort(self, port):
        if port in self._MOTEURS:
            raise MoteurExistErreur
        if port not in Moteur._PORTS:
            raise MoteurPortErreur
        del Moteur._MOTEURS[self._port]
        self._port = port
        self._MOTEURS[port] = self
        
    def setConsigne(self, consigne):
        if consigne < -100 or consigne > 100:
            raise MoteurConsigneErreur
        self._consigne = consigne
        if self.isRuning():
            if consigne > 0:
                self._pwm1.ChangeDutyCycle(100) #100, état haut
                self._pwm2.ChangeDutyCycle(100 - consigne) #ici, rapport_cyclique vaut entre 0.0 et 100.0
            elif consigne < 0:
                self._pwm1.ChangeDutyCycle(100 + consigne) #ici, rapport_cyclique vaut entre 0.0 et 100.0
                self._pwm2.ChangeDutyCycle(100) #100, état haut
            else:
                self._pwm1.ChangeDutyCycle(100)
                self._pwm2.ChangeDutyCycle(100)

    def go(self, tempsMS, consigne = 'A'):
        #le temps en ms
        if consigne != 'A':
            self.setConsigne(consigne)
        try:
            int(tempsMS)
            if tempsMS <= 0:
                raise MoteurTempsErreur
        except:
            raise MoteurTempsErreur

        self_isRuning = True
        
        if self.getConsigne() > 0:
            self._pwm1.start(100) #100, état haut
            self._pwm2.start(100 - self.getConsigne()) #ici, rapport_cyclique vaut entre 0.0 et 100.0
        elif self.getConsigne() < 0:
            self._pwm1.start(100 + self.getConsigne()) #ici, rapport_cyclique vaut entre 0.0 et 100.0
            self._pwm2.start(100) #100, état haut
        else:
            self._pwm1.start(100)
            self._pwm2.start(100)
        self.test(tempsMS)
        self_isRuning = False
    
    def test(self, tempsMS):
        time.sleep(tempsMS / 1000)
        self.stop()
    
    def stop(self):
        self._pwm1.stop()
        self._pwm2.stop()

    
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Moteur sur le port {}\n\tConsigne : {}" . format(self._port, self._consigne)
    
    def __del__(self):
        del Moteur._MOTEURS[self._port]
