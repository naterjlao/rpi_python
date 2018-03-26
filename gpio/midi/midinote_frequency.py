import math
import midi

# Define Equal Temperment Ratio and TUNING ie A_3
RATIO = math.pow(2,1.0/12)
TUNING = 440

# Define a function
def midi_frequency(note, roundFreq=True):
	distance = note - midi.A_3
	freq = TUNING * math.pow(RATIO,distance)
	if roundFreq:
		freq = round(freq)
	return  freq


