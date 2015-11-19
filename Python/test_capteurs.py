#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from TouchCapteurs import TouchCapteur

Capteur1 = TouchCapteur('1')

while 1:
    if (Capteur1.isPressed()):
        print("Le capteur est appuez")
    else:
        print("Le capteur est relaché")
