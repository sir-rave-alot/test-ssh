# from grovepi import *
import grovepi
import signal
import os

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    os._exit(0)
signal.signal(signal.SIGINT, receiveSignal)

ledbar = 5  # Connect the Grove LED Bar to digital port D5
ultrasonic_ranger = 4  # Connect the Grove Ultrasonic Ranger to digital port D4

grovepi.ledBar_init(ledbar, 0)
grovepi.ledBar_orientation(ledbar, 1)
grovepi.pinMode(ledbar, "OUTPUT")
i = 0
wert = 20

while True:

    # Read distance value from Ultrasonic 
    dist = grovepi.ultrasonicRead(ultrasonic_ranger)

    # calculation for LED Bar
    if wert < 31:
        wert = (30 - dist) / 3
    else:
        wert = 0

    if wert >= 0 and wert <= 10:
        grovepi.ledBar_setLevel(ledbar, wert)

    print wert