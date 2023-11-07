# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:01:09 2023

@author: Fujitsu
"""

# AUFGABE 1 - FAKULTÄT 


import HA_Module_mymathmodule as mm

print(mm.fac(5))


# AUFGABE 2 - EULERSCHE ZAHL


print(mm.e)


# AUFGABE 3 - IMPORT EULERSCHE ZAHL AUS MATH

import math

print(math.e)


# AUFGABE 4 - IMPORT PLATFORM

import platform

print(platform.system())         # Windows ist die Ausgabe - mein Betriebssystem


# AUFGABE 5 - IMPORT TIME

import time

print(time.ctime())           # Ausgabe ist das heutige Datum mit genauer Uhrzeit


# AUFGABE 6 - IMPORT RANDINT


from random import randint

print(mm.fac(randint(1,20)))