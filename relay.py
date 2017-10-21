from time import sleep
import RPi.GPIO as GPIO

DELAY = 0.01
CHANNEL = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)

status = True
GPIO.output(CHANNEL, status)
while True:
	try:
		sleep(DELAY)
	except KeyboardInterrupt:
		break
GPIO.output(CHANNEL, not status)
GPIO.cleanup()
