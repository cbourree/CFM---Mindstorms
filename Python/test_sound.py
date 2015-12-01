#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from SoundCapteurs import SoundCapteur
import time

GPIO.setmode(GPIO.BOARD)

SC = SoundCapteur('1')

while 1:
    print("\nTension du son :")
    print(SC.getSound())
    time.sleep(1)

GPIO.cleanup()
