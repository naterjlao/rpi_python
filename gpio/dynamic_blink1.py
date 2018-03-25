import RPi.GPIO as GPIO
import time

# Setting Numbering Declaration
GPIO.setmode(GPIO.BOARD)

# Declare Pins
led = 11

# Set Pin Modes
GPIO.setup(led, GPIO.OUT)

delay = 1.0
increase = False
upper_limit = 1.0
lower_limit = 0.05


# Blink every second and change interval
while True:
	if delay < lower_limit:
		increase = True
	elif delay > upper_limit:
		increase = False
	if increase:
		delay = delay + 0.1
	else:
		delay = delay - 0.1
	on_time = delay / 5 * 3
	off_time = delay / 5 * 2
	GPIO.output(led, GPIO.HIGH)
	time.sleep(on_time)
	GPIO.output(led, GPIO.LOW)
	time.sleep(off_time)

