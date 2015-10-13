#-*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

class MoteurExistErreur(Exception):
    #Un moteur est déjà initialisé sur ce port
    pass

class MoteurPortErreur(Exception):
    #Le port demandé n'existe pas
    pass

class MoteurVitesseErreur(Exception):
    #La vitesse n'est pas comprises entre -100 et 100
    pass

class MoteurTempsErreur(Exception):
    #Le temps n'est pas possible
    pass
 
class Moteur:
 
    _MOTEURS = {} #Liste des ports utilisé
    _PORTS = "ABC" #Liste des ports disponibles
    
    def __new__(cls, port, vitesse = 0):
        if port in cls._MOTEURS:
            raise MoteurExistErreur
        if port not in Moteur._PORTS:
            raise MoteurPortErreur
        if vitesse < -100 or vitesse > 100:
            raise MoteurVitesseError
        self = object.__new__(cls)
        self._port = port
        self._vitesse = vitesse
        cls._MOTEURS[port] = self
        return self

    def getPort(self):
        return self._port
    
    def getVitesse(self):
        return self._vitesse

    def setPort(self, port):
        if port in self._MOTEURS:
            raise MoteurExistErreur
        if port not in Moteur._PORTS:
            raise MoteurPortErreur
        del Moteur._MOTEURS[self._port]
        self._port = port
        self._MOTEURS[port] = self

    def setVitesse(self, vitesse):
        if vitesse < -100 or vitesse > 100:
            raise MoteurVitesseErreur
        self._vitesse = vitesse
        #self._pwm1.ChangeDutyCycle(nouveau_rapport_cyclique)

    def go(self, temps, vitesse = 'A'):
        #le temps en ms
        if vitesse != 'A':
            self.setVitesse(vitesse);
        try:
            int(temps)
            if temps <= 0:
                raise MoteurTempsErreur
        except:
            raise MoteurTempsErreur
        self._pwm1 = GPIO.PWM(channel, frequence)
        self._pwm1.start(rapport_cyclique) #ici, rapport_cyclique vaut entre 0.0 et 100.0
        time.sleep(5) #On attend 5 sec
        self.stop()
        
        
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Moteur sur le port {}\n\tVitesse : {}" . format(self._port, self._vitesse)
    
    def __del__(self):
        del Moteur._MOTEURS[self._port]
