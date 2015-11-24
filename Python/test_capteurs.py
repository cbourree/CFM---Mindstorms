#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from TouchCapteurs import TouchCapteur
import time

Capteur1 = TouchCapteur('1')

while 1:
    if (Capteur1.isPressed() == 1):
        print("Le capteur est appuyez")
    else:
        print("Le capteur est relaché")
    time.sleep(0.1)
