#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from LightCapteurs import LightCapteur
import time

GPIO.setmode(GPIO.BOARD)

Capteur1 = LightCapteur('1')

while 1:
    print("\nTension avec lumiere :")
    print(Capteur1.getLuminosite())
    print("Couleur : " + str(Capteur1.BlancOuNoir()))
    print("Tension sans lumiere : " + str(Capteur1.getLuminositeAmbiante()))
    time.sleep(1)

GPIO.cleanup()
