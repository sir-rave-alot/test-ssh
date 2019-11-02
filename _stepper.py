# WRAPPER CLASS FOR STEPPER MOTOR (HALF BRIDGE)
# Lucerne University of Applied Sciences , 2019
# R. Andonie (raphael.andonie@hslu.ch)

class STEPPER:
    def __init__(self, io, EN1, EN2, A1, A2, B1, B2):
        self.IO = io
        self.EN1 = EN1
        self.EN2 = EN2
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2

        self.V_CC = 12
        self.V_MAX = 5
        self.PWM_FREQ = 32000
        self.DC_MIN = 0    # smallest possible dutycycle
        self.DC_MAX = 255   # 100% Dutycycle

        self.STEP_STATE = 1

        self.V_OP = self.V_MAX
        self.DC_OP = int(self.V_OP*(self.DC_MAX / self.V_CC))

        # ENABLE POWERSTAGE
        self.IO.write(self.EN1, 1)
        self.IO.write(self.EN2, 1)
        # SET PWM FREQUENCY
        self.IO.set_PWM_frequency(self.A1, self.PWM_FREQ)
        self.IO.set_PWM_frequency(self.A2, self.PWM_FREQ)
        self.IO.set_PWM_frequency(self.B1, self.PWM_FREQ)
        self.IO.set_PWM_frequency(self.B2, self.PWM_FREQ)
        # DISABLE OUTPUTS
        self.IO.write(self.A1, 0)
        self.IO.write(self.A2, 0)
        self.IO.write(self.B1, 0)
        self.IO.write(self.B2, 0)

    def printDetails(self):
        print("~~~~~~~~~~~ MOTOR ~~~~~~~~~~~")
        print("PWM Frequency    : " + str(self.PWM_FREQ) + "Hz")
        print("Supply Voltage  : " + str(self.V_CC) + "V")
        print("Operation Voltage  : " + str(self.V_OP) + "V")
        print("~~~~~~~~~~~ ~~~~~ ~~~~~~~~~~~")

    def setPin(self, pin, val):
        self.IO.set_PWM_dutycycle(pin, val*self.DC_OP)

    def disable(self):
        # ENABLE POWERSTAGE
        self.IO.write(self.EN1, 1)
        self.IO.write(self.EN2, 1)
        # DISABLE OUTPUTS
        self.IO.write(self.A1, 0)
        self.IO.write(self.A2, 0)
        self.IO.write(self.B1, 0)
        self.IO.write(self.B2, 0)

    def stepFSM(self):
        if self.STEP_STATE == 1:
            self.setPin(self.B1, 1)  # Schaltet B ein
            self.setPin(self.B2, 0)  # Schaltet B/ aus
        elif self.STEP_STATE == 2:
            self.setPin(self.A1, 0)  # Schaltet A aus
            self.setPin(self.A2, 1)  # Schaltet A/ ein
        elif self.STEP_STATE == 3:
            self.setPin(self.B1, 0)  # Schaltet B aus
            self.setPin(self.B2, 1)  # Schaltet B/ ein
        elif self.STEP_STATE == 4:
            self.setPin(self.A1, 1)  # Schaltet A ein
            self.setPin(self.A2, 0)  # Schaltet A/ aus

    def stepForward(self):
        self.stepFSM()
        self.STEP_STATE += 1
        if self.STEP_STATE == 5:
            self.STEP_STATE = 1

    def stepBackward(self):
        self.stepFSM()
        self.STEP_STATE -= 1
        if self.STEP_STATE == 0:
            self.STEP_STATE = 4