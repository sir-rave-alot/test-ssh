import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    motor.disable()
    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import pigpio
import time

from _dcmotor import *

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
motor = DCMOTOR(io, D1, D2, A1, A2)
motor.printDetails()

v = input("Eingabe Motorenspannung {-12 .. 12V} :   ")
t = input("Eingabe Fahrtzeit {0 .. 5s} :   ")

vt_max = 12*4 # whole distance done @12V in 4sec

if(v*t) <= vt_max:
    motor.setVoltage(v)
    time.sleep(t)
else:
    print "Product [Velocity] x [Time] too high!!"
    print "Abort."

motor.disable()
###### YOUR CODE ENDS HERE ####
