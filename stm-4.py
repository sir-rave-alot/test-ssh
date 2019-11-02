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
A1 = 20  # A  or M1
A2 = 21  # A/ or M2
B1 = 6  # B  or M3
B2 = 13  # B/ or M4
D1 = 12  # N1 motordriver Enable 1
D2 = 26  # N2 motordriver Enable 2

# GPIO handler object
io = pigpio.pi()

# create dc motor handler object
motor = STEPPER(io, D1, D2, A1, A2, B1, B2)
motor.printDetails()

t = 0.1
f = 1 / t
f_max = 1000

steps_max = 14500  # whole distance

while True:
    steps = input("How many steps do you want to do ?  ")

    if (abs(steps) > steps_max):
        print "Too many steps !!"
        print "Abort."
    else:
        for stp in range(0, abs(steps)):
            if steps > 0:
                motor.stepForward()
            else:
                motor.stepBackward()

            time.sleep(t)

            if f < f_max:
                f = f + 100
                t = 1 / f

        stp = 0
        # reset ramp
        t = 0.1
        f = 1 / t

    motor.disable()
    motor.disable()
###### YOUR CODE ENDS HERE ######
