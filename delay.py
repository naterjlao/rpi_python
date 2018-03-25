import time
import sys

# Counter variable
seconds = 0
milisec = 0

while True:
	print('{:02d}:{:02d}\r'.format(seconds,milisec)),
	sys.stdout.flush()
	milisec = milisec + 1
	if milisec == 100:
		seconds = seconds + 1
		milisec = 0
	time.sleep(.01) # Delay for 1 second


