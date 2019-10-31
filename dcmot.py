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
import grovepi
from _dcmotor import *

# GPIO handler object "io"
io = pigpio.pi()

# configure IR proximity sensor
sensor = 0
grovepi.pinMode(sensor, "INPUT")    # analog input 0
v_adc_ref = 5                       # reference voltage of ADC = 5v
sensor_value = 0                    # variable allocation for raw value

# Pin Zuordnung
A1 = 20 				#A  oder M1
A2 = 21  				#A/ oder M2
B1 = 6  				#B  oder M3
B2 = 13 				#B/ oder M4
D1 = 12 				#N  -> Schaltet die Motortreiber ein
D2 = 26 				#N/ -> Schaltet die Motortreiber ein

motor = DCMOTOR(io, D1, D2, A1, A2)
motor.printDetails()

while True:
    v = input("Dutycycle ? : ")
    motor.setDC(v)
    pass

'''
#for i in range(0,10):
while True:
    # data aquisition
    sensor_value = grovepi.analogRead(sensor)  # read infrared proximity
    sensorwert = (float)(sensor_value) * v_adc_ref / 1024
    dist = 2 * round(1.6361 * sensorwert * sensorwert - 12.745 * sensorwert + 24.26, 3)
    #print dist
    #time.sleep(0.05)

    # error calculationd
    e = d_w - dist

###### YOUR CODE ENDS HERE ####
'''