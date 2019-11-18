import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    motor.disable()
    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import pigpio
import grovepi
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

# configure IR proximity sensor
sensor = 0
grovepi.pinMode(sensor, "INPUT")    # analog input 0
v_adc_ref = 5                       # reference voltage of ADC = 5v
sensor_value = 0                    # variable allocation for raw value

## TODO: REPLACE (a,b) WITH YOUR CALIBRATION VALUES
a = 7.18854109485e-05
b = 0.00181664284792

reached = False
reachCounter = 0

Tc = float(0.01)
up = float(0)
u = float(0)
dist = float(0)

K_p = 0.1
uf = 5.4
sign = 0


while (True):
    print 'Format above:'
    print '[distance] ; [motor voltage] '
    print "x = ", dist
    dist_w = input("Position ? {10..50}mm")

    while (reached != True):
        # data aquisition
        sensor_value = grovepi.analogRead(sensor)  # read infrared proximity
        dist = round((((1.0/sensor_value) - b) / a),0)

        # distance error
        e = float(dist_w - dist)

        # proportional share
        up = float(K_p*e)

        # sum shares
        if (e != 0):
            sign = float(e/abs(e))

        u = float(up + sign*uf)

        if (u > 0):
            u = 3+u*(9.0/12.0)
        else:
            u = -3 + u * (9.0 / 12.0)

        # set control variable
        motor.setVoltage(u)

        if(e == 0):
            reachCounter += 1
        else:
            reachCounter = 0

        if(reachCounter > 5):
            reached = True

        print dist, ";", u

    motor.disable()
    reached = False

###### YOUR CODE ENDS HERE ####
