import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    io.write(D1, 0)  # Motortreiber ausschalten -> 0
    io.write(D2, 0)  # Motortreiber ausschalten -> 0
    os._exit(0)

signal.signal(signal.SIGINT, receiveSignal)

###### YOUR CODE GOES HERE ######
import pigpio
import time
import grovepi

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

d_w = input("Enter target Position : ")

io.write(D1,1)
io.write(D2,1)

io.write(A2,0)
io.set_PWM_frequency(A1, 2400)
io.set_PWM_dutycycle(A1, 255/2)

while True:
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