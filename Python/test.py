#!/usr/bin/python
#-*- coding: utf-8 -*-

from Moteurs import Moteur

A = Moteur('A')
A.go(50000, 80)

B = Moteur('B', -50)
B.go(50000)

GPIO.cleanup()
