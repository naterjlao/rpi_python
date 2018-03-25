import RPi.GPIO as GPIO
import time
import sys

# Setting Numbering Declaration
GPIO.setmode(GPIO.BOARD)

# Declare Pins
led = 11

# Set Pin Modes
GPIO.setup(led, GPIO.OUT)

upper_limit = 2.0
lower_limit = 0.05
delay = upper_limit
increase = False
interval = upper_limit * 2 # The interval for every change in speed
max_iterations = 100

# Function defined blink
def blink(delay):
	on_time = delay / 5 * 3
	off_time = delay / 5 * 2
	GPIO.output(led, GPIO.HIGH)
	time.sleep(on_time)
	GPIO.output(led, GPIO.LOW)
	time.sleep(off_time)

# Blink every second and change interval
while True:
	if delay <= lower_limit:
		increase = True
	elif delay >= upper_limit:
		increase = False
	if increase:
		delay = delay + 0.1
	else:
		delay = delay - 0.1

	iterations = int(interval / delay)
	if iterations > max_iterations:
		iterations = max_iteration
	i = 0
	while i < iterations:
		blink(delay)
		i = i + 1
