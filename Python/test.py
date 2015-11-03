#!/usr/bin/python
#-*- coding: utf-8 -*-
import Moteurs

A = Moteurs.Moteur('A', 50)
print(A.getConsigne())

A.go(10, 100)
