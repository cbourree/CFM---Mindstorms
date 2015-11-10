#!/usr/bin/python
#-*- coding: utf-8 -*-

from Moteurs import Moteur

A = Moteur('A', -80)
A.go(50000)

B = Moteur('B')
B.go(5000, 50)

GPIO.cleanup()
