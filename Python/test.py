#!/usr/bin/python
#-*- coding: utf-8 -*-

from Moteurs import Moteur

GPIO.setmode(GPIO.BOARD)

print("Initialisation du moteur A...")
A = Moteur('A', -80)
A.runMS(50000)
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

print("Initialisation du moteur B...")
B = Moteur('B')
B.runMS(5000, 50)
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

print("Initialisation du moteur C...")
C = Moteur('C')
C.setConsigne(-50)
C.runMS(5000)
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

time.sleep(5)
print("5 secondes plus tard...")
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

time.sleep(5)
print("Ecnore 5 secondes plus tard...")
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

print("On attend que le moteur s'arrête")
A.waitStop()
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

print("On relance le moteur B")
B.run(10)
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

time.sleep(5)
print("5 secondes plus tard...")
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

B.stop()
print("Arrêt du moteur B")
print("Moteur A" + A.isRuning() + "Moteur B" + B.isRuning() + "Moteur C" + C.isRuning())

GPIO.cleanup()
