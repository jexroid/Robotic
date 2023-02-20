from gpiozero import Motor
import RPi.GPIO as gpio
import time


stepper_pins = (26 , 19 , 13 , 6)
LED = (21)

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(stepper_pins, gpio.OUT)
gpio.setup(LED, gpio.OUT)



while True:
        gpio.output(LED, gpio.HIGH)
        time.sleep(0.2)
        gpio.output(LED, gpio.LOW)
        time.sleep(0.2)
        gpio.output(stepper_pins, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
        time.sleep(0.2)
        gpio.output(stepper_pins, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
        time.sleep(0.2)
        gpio.output(stepper_pins, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
        time.sleep(0.2)
        gpio.output(stepper_pins, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
        time.sleep(0.2)