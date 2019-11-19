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

# GPIO handler object
io = pigpio.pi()

# configure IR proximity sensor
sensor = 0
grovepi.pinMode(sensor, "INPUT")    # analog input 0
v_adc_ref = 5                       # reference voltage of ADC = 5v
sensor_value = 0                    # variable allocation for raw value
dist = float(0)

nof_samples = 10
x_min = float(0)
x_max = float(45)

v_m_min = float(0)
v_m_max = float(0)

inp = None

print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print '~~~~~~ IR-CALIBRATION ~~~~~~'
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'

while(inp != 'start'):
    print 'Move to ', x_min, 'mm (MOST APPROXIMATE TO SENSOR)'
    inp = raw_input('Enter "start" to start measurements.')

for i in range(0,nof_samples):
    sensor_value = grovepi.analogRead(sensor)
    v_m_min += sensor_value
    print 'ADC-Value [', i, '] =' , sensor_value
    time.sleep(0.5)

i = 0
inp = None

while(inp != 'start'):
    print 'Move to ', x_max, 'mm (MOST DISTANCE FROM SENSOR)'
    inp = raw_input('Enter "start" to start measurements.')

for i in range(0,nof_samples):
    sensor_value = grovepi.analogRead(sensor)
    v_m_max += sensor_value
    print 'ADC-Value [', i, '] =', sensor_value
    time.sleep(0.5)

#####
v_m_min = v_m_min/nof_samples
v_m_max = v_m_max/nof_samples

D_MIN = x_min
D_MAX = x_max

S_MIN= 1.0/v_m_min
S_MAX = 1.0/v_m_max

# RECIPROCAL SLOPE
a = (S_MAX - S_MIN)/(D_MAX - D_MIN);
# RECIPROCAL OFFSET
b1 = S_MAX - a*D_MAX
b2 = S_MIN - a*D_MIN
b = (b1+b2)/2

#####
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print 'Mean (Min) = ', v_m_min
print 'Mean (Max) = ', v_m_max
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print 'Backcalculation Model: '
print 'x_estimation = (1/v-b)/a'
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print 'a = ', a
print 'b = ', b
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print 'Copy these values into : '
print 'ps-2.py '
print 'p-control-1.py '
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'
print 'Done.'
print '~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~'

###### YOUR CODE ENDS HERE ####
