#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from UltrasonicCapteurs import UltrasonicCapteur
import time

GPIO.setmode(GPIO.BOARD)


#UC = UltrasonicCapteur('3')

#while 1:
#    print("\nDistance :")
#    print(UC.getDistance())
#    time.sleep(1)

GPIO.cleanup()

