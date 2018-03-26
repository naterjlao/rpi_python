import RPi.GPIO as GPIO
import time

# SEt numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin number and set io
pwm_pin = 18
GPIO.setup(pwm_pin, GPIO.OUT)


# Pulse Width Modulation
freq = 220
hi_freq = freq * 2
lo_freq = freq / 2
pwm = GPIO.PWM(pwm_pin,freq)
delay = 0.1
increase = True
pwm.start(50)

while True:
	if freq > hi_freq:
		increase = False
	elif freq < lo_freq:
		increase = True
	if increase:
		freq = freq + 10
	else:
		freq = freq - 10
	pwm.ChangeFrequency(freq)
	time.sleep(delay)
