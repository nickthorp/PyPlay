__author__ = 'nthorp'

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably from permission access.")

GPIO.setmode(GPIO.BCM)

# Add a new channel for output to the led
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)

GPIO.cleanup()
