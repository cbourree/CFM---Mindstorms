#!/usr/bin/python
#-*- coding: utf-8 -*-

from Moteurs import Moteur

GPIO.setmode(GPIO.BOARD)

A = Moteur('A', -80)
A.go(50000)

B = Moteur('B')
B.go(5000, 50)

B.go(5000, 40)

GPIO.cleanup()
