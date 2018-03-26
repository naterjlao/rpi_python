import midi
import RPi.GPIO as GPIO


# This will read a midi file and play it through BCM 18
# Setup GPIO
GPIO.setmode(GPIO.BCM)
pwm_pin = 18
GPIO.setup(pwm_pin, GPIO.OUT)


# Read the midi file
file_name = "mary.mid"
tempo = 120
pattern = midi.read_midifile(file_name)
delay = tempo / (60.0 * pattern.resolution)
tracks = pattern.pop()
#print tracks
#print delay

# Pulse Width Modulation
duty = 50
pwm = GPIO.PWM(pwm_pin,440)
pwm.start(duty)

# This iterates through the track and skips all non-note events
event = tracks.pop(0)
while not isinstance(event,midi.NoteOnEvent):
	print event
	event = tracks.pop(0)

# Event is now set to the FIRST Note event
print event
