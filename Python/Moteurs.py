#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from threading import Thread

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

class ThreadGo(Thread):
#Run non bloquant
    
    def __init__(self, mo, tempsMS):
        Thread.__init__(self)
        self._mo = mo 
        self._tempsMS = tempsMS

    def run(self):
        #Appellé pour lancer le moteur sans arrêt tempo
        self._mo._isRuning = True
        if self._mo.getConsigne() > 0:
            self._mo._pwm1.start(100) #100, état haut
            self._mo._pwm2.start(100 - self._mo.getConsigne()) #ici, rapport_cyclique vaut entre 0.0 et 100.0
        elif self._mo.getConsigne() < 0:
            self._mo._pwm1.start(100 + self._mo.getConsigne()) #ici, rapport_cyclique vaut entre 0.0 et 100.0
            self._mo._pwm2.start(100) #100, état haut
        else:
            self._mo._pwm1.start(100)
            self._mo._pwm2.start(100)
        
        time.sleep(self._tempsMS / 1000)
        self._mo.stop()
    
class Moteur():
 
    _MOTEURS = {} #Liste des ports utilisé
    _PORTS = "ABC" #Liste des ports disponibles
    
    def __new__(cls, port, consigne = 0):
        #Initialisation du nouveau moteur
        if port in cls._MOTEURS: #Si le port est déjà pris
            raise MoteurExistErreur
        if port not in Moteur._PORTS: #Si le port est dispo
            raise MoteurPortErreur
        if consigne < -100 or consigne > 100: #Si la vitesse est comprise dans [-100;100]
            raise MoteurConsigneError
        self = object.__new__(cls)
        self._port = port
        self._isRuning = False
        self._consigne = consigne
        cls._MOTEURS[port] = self
        if port == 'A':
            pinA = 33
            pinB = 35
            self._pinTacho1 = 7
            self._pinTAcho2 = 11
        elif port == 'B':
            pinA = 37
            pinB = 40
        else:
            pinA = 38
            pinB = 36
        GPIO.setup(pinA, GPIO.OUT) #On initialise les pins en sortie
        GPIO.setup(pinB, GPIO.OUT)
        self._pwm1 = GPIO.PWM(pinA, 1000) #On les mets en tant que sortie PWMs
        self._pwm2 = GPIO.PWM(pinB, 1000)
        GPIO.setup(self._pinTacho1, GPIO.IN) #On initialise les entrée pour récupéré signal tacho
        GPIO.setup(self._pinTacho2, GPIO.IN)
        return self

    def getPort(self):
        #Return le port du moteur
        return self._port
    
    def getConsigne(self):
        #Return la consigne, comprise entre -100 et 100
        return self._consigne

    def isRuning(self):
        #Return True si le moteur est en marche, False sinon
        return self._isRuning

    def setPort(self, port):
        #Change le port du moteur
        if port in self._MOTEURS:
            raise MoteurExistErreur
        if port not in Moteur._PORTS:
            raise MoteurPortErreur
        del Moteur._MOTEURS[self._port]
        self._port = port
        self._MOTEURS[port] = self
        
    def setConsigne(self, consigne):
        #Change la consigne du moteur
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

    def runMS(self, tempsMS, consigne = 'A'):
        #Lance les moteurs pour un certain temps tempsMS,temps en ms, et une certaine consigne consigne
        if consigne != 'A':
            self.setConsigne(consigne)
        try:
            int(tempsMS)
            if tempsMS <= 0:
                raise MoteurTempsErreur
        except:
            raise MoteurTempsErreur
        thread = ThreadGo(self, tempsMS)
        thread.start()

    def runInfini(self, consigne):
        #Lance le moteur avec une certaine consigne consigne, doit être arrêté avec stop()
        if consigne != 'A':
            self.setConsigne(consigne)
        self._isRuning = True
        
        if self.getConsigne() > 0:
            self._pwm1.start(100) #100, état haut
            self._pwm2.start(100 - self.getConsigne()) #ici, rapport_cyclique vaut entre 0.0 et 100.0
        elif mo.getConsigne() < 0:
            self._pwm1.start(100 + self.getConsigne()) #ici, rapport_cyclique vaut entre 0.0 et 100.0
            self._pwm2.start(100) #100, état haut
        else:
            self._pwm1.start(100)
            self._pwm2.start(100)
        

    def waitStop(self):
        #Attend que le moteur s'arrête
        while self.isRuning():
            time.sleep(0.001)
    
    def stop(self):
        #Arrête les moteurs
        self._pwm1.stop()
        self._pwm2.stop()
        self._isRuning = False

    def getVitesse(self):
        #Return la vitesse mesuré des moteurs
        GPIO.wait_for_edge(self._pinTacho1, GPIO.RISING)
        t0 = time.clock()
        GPIO.wait_for_edge(self._pinTacho1, GPIO.RISING)
        t1 = time.clock()
        temps = t1 - t0
        print("Temps : ", temps)
        
        
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Moteur sur le port {}\n\tConsigne : {}" . format(self._port, self._consigne)
    
    def __del__(self):
        del Moteur._MOTEURS[self._port]
