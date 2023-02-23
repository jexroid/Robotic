"""
MOVING THE DC MOTOR in clock and clockwise direction 
"""


class motor:
    global DC_motor
    import RPi.GPIO as GPIO


    DC_motor = (5 , 6)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DC_motor, GPIO.OUT)

    
    def clock(time):
        import RPi.GPIO as GPIO
        while (certainity < time):
            GPIO.output(DC_motor , (GPIO.HIGH, GPIO.LOW))

            certainity = certainity + 1
        GPIO.cleanup()
    def clockwise(time):
        import RPi.GPIO as GPIO
        while (certainity < time):
            GPIO.output(DC_motor , (GPIO.LOW, GPIO.HIGH))

            certainity = certainity + 1
        GPIO.cleanup()
