import RPi.GPIO as GPIO

class PrinterGPIO():
    def __init__(self, gpio = 15, bcm = True):
        self.gpio = gpio

        if bcm:
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.gpio, GPIO.OUT)

    def setNewState(self, oldstate):
        GPIO.output(self.gpio, not oldstate)

    def __del__(self):
        GPIO.cleanup()
