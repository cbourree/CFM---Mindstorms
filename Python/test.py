#!/usr/bin/python
#-*- coding: utf-8 -*-

from Moteurs import Moteur

A = Moteur('A', -50)
A.go(5000)

B = Moteur('B')
B.go(5000, 50)

GPIO.cleanup()
