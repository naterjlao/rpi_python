import RPi.GPIO as GPIO
import time
import math

# SEt numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin number and set io
pwm_pin = 18
GPIO.setup(pwm_pin, GPIO.OUT)


# Pulse Width Modulation
semitone = math.pow(2,1.0/12)
freq = 220
hi_freq = freq * 2
lo_freq = freq / 2
pwm = GPIO.PWM(pwm_pin,freq)
delay = 0.1
increase = True
pwm.start(50)

def noteUp(freq):
	return round(freq * semitone)

def noteDown(freq):
	return round(freq / semitone)

while True:
	if freq >= hi_freq:
		increase = False
	elif freq <= lo_freq:
		increase = True
	if increase:
		freq = noteUp(freq)
	else:
		freq = noteDown(freq)
	pwm.ChangeFrequency(freq)
	time.sleep(delay)
