import RPi.GPIO as GPIO

class PrinterGPIO():
    def __init__(self, gpio = 18, bcm = True):
        self.gpio = gpio

        if bcm:
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.gpio, GPIO.OUT)

    def setNewState(self, newstate):
        GPIO.output(self.gpio, newstate)

    def __del__(self):
        GPIO.cleanup()
