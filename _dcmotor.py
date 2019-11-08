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

        self.V_CC = 12
        self.PWM_FREQ = 64000
        #self.DC_MIN = 0    # smallest possible dutycycle
        self.DC_MAX = 255   # 100% Dutycycle

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
        print("~~~~~~~~~~~ MOTOR ~~~~~~~~~~~")
        print("GPIO Pins        : " + str(self.X1) + " ; " + str(self.X2))
        print("PWM Frequency    : " + str(self.PWM_FREQ) + "Hz")
        print( "Supply Voltage  : " + str(self.V_CC) + "V")
        print("~~~~~~~~~~~ ~~~~~ ~~~~~~~~~~~")

    def setVoltage(self, v):
        _v = int(v*(self.DC_MAX / self.V_CC))

        if(abs(_v) > self.DC_MAX):
            print("Voltage too high!")
            _v = (_v/abs(_v)) * float(self.DC_MAX)

        if(v > 0):
            self.IO.write(self.X2, 0)
            self.IO.set_PWM_dutycycle(self.X1, abs(_v))
        else:
            self.IO.write(self.X1, 0)
            self.IO.set_PWM_dutycycle(self.X2, abs(_v))

    def disable(self):
        # ENABLE POWERSTAGE
        self.IO.write(self.EN1, 1)
        self.IO.write(self.EN2, 1)
        # DISABLE OUTPUTS
        self.IO.write(self.X1, 0)
        self.IO.write(self.X2, 0)