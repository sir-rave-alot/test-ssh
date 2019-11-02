import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    ###### YOUR CODE GOES HERE ######
    motor.disable()
    motor.disable()
    ###### YOUR CODE ENDS HERE ######

    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import pigpio
import time

from _stepper import *

# Pin assignments
A1 = 20 #A  or M1
A2 = 21 #A/ or M2
B1 = 6  #B  or M3
B2 = 13 #B/ or M4
D1 = 12 #N1 motordriver Enable 1
D2 = 26 #N2 motordriver Enable 2

# GPIO handler object
io = pigpio.pi()

# create dc motor handler object
motor = STEPPER(io, D1, D2, A1, A2, B1, B2)
motor.printDetails()


t = 0.1
f = 1/t
f_max = 1000

while(True): 			#Endlosschleife

    motor.setPin(B1,1) 		#Schaltet B ein
    motor.setPin(B2,0) 		#Schaltet B/ aus
    time.sleep(t) 		    #Wartezeit in Sekunden bis zum naechsten Step

    motor.setPin(A1,0)		#Schaltet A aus
    motor.setPin(A2,1)		#Schaltet A/ ein
    time.sleep(t)		    #Wartezeit in Sekunden bis zum naechsten Step

    motor.setPin(B1,0)		#Schaltet B aus
    motor.setPin(B2,1)		#Schaltet B/ ein
    time.sleep(t)		    #Wartezeit in Sekunden bis zum naechsten Step

    motor.setPin(A1,1)		#Schaltet A ein
    motor.setPin(A2,0)		#Schaltet A/ aus
    time.sleep(t)		    #Wartezeit in Sekunden bis zum naechsten Step

    if f < f_max:
        f = f + 100
        t = 1/f

###### YOUR CODE ENDS HERE ######