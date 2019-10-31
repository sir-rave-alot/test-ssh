import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    pi1.write(D1, 0)  # Motortreiber ausschalten -> 0
    pi1.write(D2, 0)  # Motortreiber ausschalten -> 0
    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import pigpio
import time

import pigpio
import time

pi1 = pigpio.pi() 			# Erstellt ein Objekt der Klasse pi

#Pin Zuordnung
A1 = 20 				#A  oder M1
A2= 21  				#A/ oder M2
B1 = 6  				#B  oder M3
B2 = 13 				#B/ oder M4
D1 = 12 				#N  -> Schaltet die Motortreiber ein
D2 = 26 				#N/ -> Schaltet die Motortreiber ein

pi1.write(D1,1)			#Motortreiber einschalten -> 1
pi1.write(D2,1)			#Motortreiber einschalten -> 1

print("Press Ctrl+C to interrupt")

t = 0.1
f = 1/t

while(True): 			#Endlosschleife

    pi1.write(B1,1) 		#Schaltet B ein
    pi1.write(B2,0) 		#Schaltet B/ aus
    time.sleep(t) 		#Wartezeit in Sekunden bis zum naechsten Step

    pi1.write(A1,0)			#Schaltet A aus
    pi1.write(A2,1)			#Schaltet A/ ein
    time.sleep(t)		#Wartezeit in Sekunden bis zum naechsten Step

    pi1.write(B1,0)			#Schaltet B aus
    pi1.write(B2,1)			#Schaltet B/ ein
    time.sleep(t)		#Wartezeit in Sekunden bis zum naechsten Step

    pi1.write(A1,1)			#Schaltet A ein
    pi1.write(A2,0)			#Schaltet A/ aus
    time.sleep(t)		#Wartezeit in Sekunden bis zum naechsten Step

    if f < 1000:
        f = f + 100
        t = 1/f

###### YOUR CODE ENDS HERE ######