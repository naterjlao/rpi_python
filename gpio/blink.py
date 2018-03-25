import RPi.GPIO as GPIO
import time

# Setting Numbering Declaration
GPIO.setmode(GPIO.BOARD)

# Declare Pins
led = 11

# Set Pin Modes
GPIO.setup(led, GPIO.OUT)

on_time = 0.3
off_time = 0.2


# Blink every second
while True:
	GPIO.output(led, GPIO.HIGH)
	time.sleep(on_time)
	GPIO.output(led, GPIO.LOW)
	time.sleep(off_time)

