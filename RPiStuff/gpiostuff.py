__author__ = 'nthorp'

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably from permission access.")

GPIO.setmode(GPIO.BCM)

# Add a new channel for output to the led
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)

p = GPIO.PWM(18, 50)
p.start(3)
p.ChangeDutyCycle(7.5)
p.stop()
GPIO.cleanup()
