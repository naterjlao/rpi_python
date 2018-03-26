import RPi.GPIO as GPIO
import sys
import time

# Set Numbering
GPIO.setmode(GPIO.BOARD)

pwm_pin = 12

# Set output
GPIO.setup(pwm_pin, GPIO.OUT)

# Pulse Width Modulation
pwm = GPIO.PWM(pwm_pin,220)
duty_cycle = 50
pwm.start(duty_cycle)
increase = True
change_rate = 0.1

while True:
	if increase:
		duty_cycle = duty_cycle + 1
	else:
		duty_cycle = duty_cycle - 1
	if duty_cycle % 100 == 0:
		increase = not increase
	print('{}\r'.format(duty_cycle)),
	sys.stdout.flush()
	time.sleep(change_rate)
	pwm.ChangeDutyCycle(duty_cycle)


