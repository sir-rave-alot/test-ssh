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

toggler = 0
reached = False
reachCounter = 0

Tc = float(0.01)
up = float(0)
ui = float(0)
u = float(0)
dist = float(0)

K_p = input("Kp ?")
uf = input("U_f ?")
K_i = 0
sign = 0


while (True):
    print "x = ", dist
    dist_w = input("Position ? {0..50}mm")

    while (reached != True):
        # data aquisition
        sensor_value = grovepi.analogRead(sensor)  # read infrared proximity
        dist = round(77.77777778 + (float(sensor_value) * (-0.15873016)),0)

        # distance error
        e = float(dist_w - dist)

        # proportional share
        up = float(K_p*e)

        # integral share
        ui = ui + float(Tc*e*K_i)

        # sum shares
        if (e != 0):
            sign = float(e/abs(e))

        u = float(up + ui + sign*uf)

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
        #time.sleep(0.005)

        # TESTPIN
        if (toggler == 0):
            toggler = 1
        else:
            toggler = 0
        #
        io.write(B1, toggler)

    motor.disable()
    reached = False
    ui = 0

###### YOUR CODE ENDS HERE ####
