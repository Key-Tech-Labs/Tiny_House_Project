"""Module that will hold code to test PIR sensor functionality."""

import RPi.GPIO as GPIO
from time import sleep

pir_sensor = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0

try:
    while True:
        sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print('MOTION DETECTED!')
            sleep(3)
            print('RESETTING NOW...')
            sleep(1)
except(KeyboardInterrupt):
    print('Monitoring process: terminated.')
    GPIO.cleanup()
