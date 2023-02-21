class motor:
    global LED , DC_motor , encoder
    import RPi.GPIO as GPIO


    DC_motor = (5 , 6)
    LED = (21)
    encoder = 12

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DC_motor, GPIO.OUT)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(encoder , GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def clock():
        stateLast = GPIO.input(encoder)
        rotationCount = 0
        stateCount = 0  
        stateCountTotal = 0
        try:
            import RPi.GPIO as GPIO
            import time

            while True:
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(LED, GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(DC_motor, (GPIO.HIGH , GPIO.LOW))
        except KeyboardInterrupt:
            GPIO.cleanup()

