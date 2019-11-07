import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import pigpio
import grovepi
import time

# configure IR proximity sensor
sensor = 0
grovepi.pinMode(sensor, "INPUT")    # analog input 0
v_adc_ref = 5                       # reference voltage of ADC = 5v
sensor_value = 0                    # variable allocation for raw value



n_buf = 11
nh_buf = 6
sensor_buf = [0] * n_buf
avg_buf = [0] * n_buf
for i in range(0, n_buf-1):
    sensor_value = grovepi.analogRead(sensor)  # read infrared proximity
    sensorwert = (float)(sensor_value) * v_adc_ref / 1024
    dist = 2 * round(1.6361 * sensorwert * sensorwert - 12.745 * sensorwert + 24.26, 3)
    sensor_buf[i] = dist


while True:
    # data aquisition
    sensor_value = grovepi.analogRead(sensor)  # read infrared proximity
    #sensorwert = (float)(sensor_value) * (float)(v_adc_ref) / (float)(1024)
    #dist = 2 * round(1.6361 * sensorwert * sensorwert - 12.745 * sensorwert + 24.26, 3)

    dist = round(77.77777778 + (float(sensor_value) * (-0.15873016)),0)
    #sensor_buf[1:] + [dist]

    print "D ->: " , dist
    time.sleep(1)


    avg_buf = sensor_buf.sort()

###### YOUR CODE ENDS HERE ####
