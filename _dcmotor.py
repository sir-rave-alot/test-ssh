# WRAPPER CLASS FOR DC MOTOR (HALF BRIDGE)
# Lucerne University of Applied Sciences , 2019
# R. Andonie (raphael.andonie@hslu.ch)

class DCMOTOR:
    def __init__(self, io, EN1, EN2, X1, X2):
        self.IO = io
        self.EN1 = EN1
        self.EN2 = EN2
        self.X1 = X1
        self.X2 = X2

        self.PWM_FREQ = 3200

        # ENABLE POWERSTAGE
        self.IO.write(self.EN1, 1)
        self.IO.write(self.EN2, 1)
        # SET PWM FREQUENCY
        self.IO.set_PWM_frequency(self.X1, self.PWM_FREQ)
        self.IO.set_PWM_frequency(self.X2, self.PWM_FREQ)
        # DISABLE OUTPUTS
        self.IO.write(self.X1, 0)
        self.IO.write(self.X2, 0)

    def printDetails(self):
        print("GPIO Pins        : " + str(self.X1) + " ; " + str(self.X2))
        print("PWM Frequency    : " + str(self.X1))

    def setDC(self, v):
        print("setDC to " + str(v))
        self.IO.set_PWM_dutycycle(self.X1, v)

    def disable(self):
        # ENABLE POWERSTAGE
        self.IO.write(self.EN1, 1)
        self.IO.write(self.EN2, 1)
        # DISABLE OUTPUTS
        self.IO.write(self.X1, 0)
        self.IO.write(self.X2, 0)