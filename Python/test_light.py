#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from TouchCapteurs import TouchCapteur
from LightCapteurs import LightCapteur
import time

Capteur1 = LightCapteur('1')

while 1:
    Capteur1.getLuminosite()
    time.sleep(0.4)
