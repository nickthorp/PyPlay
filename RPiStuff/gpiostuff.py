__author__ = 'nthorp'

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably from permission access.")

GPIO.setmode(GPIO.BCM)

# Add a new channel for output to the led
 GPIO.setup(23, GPIO.OUT)
 GPIO.output(23, GPIO.HIGH)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(3)
loopctrl = True
while loopctrl:
    angle = input('Give an angle between 0 and 150 degrees or type EXIT to quit: ')

    if angle.isnumeric():
        timing = int(angle) / 100 + 0.6
        if int(angle) < 0 or int(angle) > 150:
            print("Please enter a value between 0 and 150 degrees!\n")
            continue
        else:
            #p.ChangeDutyCycle(timing)
            print(timing)
    elif angle.isalpha():
        if angle.upper() == 'EXIT':
            loopctrl = False
        else:
            print("Please enter a valid angle or \'Exit\' to quit")
p.ChangeDutyCycle(7.5)
p.stop()
GPIO.cleanup()
