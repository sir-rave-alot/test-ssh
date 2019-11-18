
import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import grovepi
import time


# configure IR proximity sensor
sensor = 0
grovepi.pinMode(sensor, "INPUT")    # analog input 0
v_adc_ref = 5                       # reference voltage of ADC = 5v
sensor_value = 0                    # variable allocation for raw value
x_estimated = float(0)

## TODO: REPLACE (a,b) WITH YOUR CALIBRATION VALUES
a = 7.18854109485e-05
b = 0.00181664284792

print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print '~~~~~~ IR-VERIFICATION ~~~~~~'
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'


while True:
    sensor_value = float(grovepi.analogRead(sensor))
    x_estimated = ((1.0/sensor_value) - b) / a
    print 'x_estimation = ', round(x_estimated, 3), ' mm'
    time.sleep(1)

###### YOUR CODE ENDS HERE ####





