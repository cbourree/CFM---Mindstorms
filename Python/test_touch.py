#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from TouchCapteurs import TouchCapteur
import time

Capteur1 = TouchCapteur('1')
Capteur3 = TouchCapteur('3')
Capteur2 = TouchCapteur('2')
Capteur4 = TouchCapteur('4')
while 1:
    if (Capteur1.isPressed() == 1):
        print("Port 1 appuyé")
    else:
        print("Port 1 relaché")
    if (Capteur3.isPressed() == 1):
        print("Port 3 appuyé")
    else:
        print("Port 3 relaché")
    if (Capteur4.isPressed() == 1):
        print("Port 4 appuyé")
    else:
        print("Port 4 relaché")
    if (Capteur2.isPressed() == 1):
        print("Port 2 appuyé")
    else:
        print("Port 2 relaché")

    time.sleep(1)
