"""
import RPi.GPIO as GPIO

GPIO.setup(12, GPIO.IN)                    # broche 12 est une entree numerique
GPIO.setup(12, GPIO.OUT)                   # broche 12 est une sortie numerique
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)# broche 12 est une sortie initialement a l'etat haut

GPIO.input(12) #Lire l'état du port 12

GPIO.output(12, GPIO.LOW) #Passage de la sortie à l'état bas


GPIO.cleanup()#Pour restaurer les ports comme au début du programme
"""


