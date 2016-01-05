#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from Moteurs import Moteur
import time

GPIO.setmode(GPIO.BOARD)

print("Initialisation du moteur A...")
A = Moteur('A')
B = Moteur('B')
C = Moteur('C', 80)
A.runMS(15000, 50)
print("Moteur A : " + str(A.isRuning()) + "Moteur B : " + str(B.isRuning()) + "Moteur C : " + str(C.isRuning()))

print("Initialisation du moteur B...")
B.runMS(15000, 50)
print("Moteur A : " + str(A.isRuning()) + "Moteur B : " + str(B.isRuning()) + "Moteur C : " + str(C.isRuning()))

print("Initialisation du moteur C...")
C.setConsigne(50)
C.runMS(15000)
print("Moteur A" + str(A.isRuning()) + "Moteur B" + str(B.isRuning()) + "Moteur C" + str(C.isRuning()))
time.sleep(5)
print("5 secondes plus tard...")
print("Moteur A" + str(A.isRuning()) + "Moteur B" + str(B.isRuning()) + "Moteur C" + str(C.isRuning()))

time.sleep(5)
print("Ecnore 5 secondes plus tard...")
print("Moteur A" + str(A.isRuning()) + "Moteur B" + str(B.isRuning()) + "Moteur C" + str(C.isRuning()))

print("On attend que le moteur s'arrête")
A.waitStop()
print("Moteur A" + str(A.isRuning()) + "Moteur B" + str(B.isRuning()) + "Moteur C" + str(C.isRuning()))

print("On relance le moteur B")
B.runInfini(10)
print("Moteur A" + str(A.isRuning()) + "Moteur B" + str(B.isRuning()) + "Moteur C" + str(C.isRuning()))

time.sleep(5)
print("5 secondes plus tard...")
print("Moteur A" + str(A.isRuning()) + "Moteur B" + str(B.isRuning()) + "Moteur C" + str(C.isRuning()))

B.stop()
print("Arrêt du moteur B")

GPIO.cleanup()
