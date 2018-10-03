"""Module to test proper LED hardware configuration on Raspberry Pi 3."""

import RPi.GPIO as GPIO
import time


# Configuration for RPi GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

hello_world = 'Hello World'

# Dict that holds morse code
morse_code = ['....', '.', '.-..', '.-..', '---', ' ', '.--', '---', '.-.', '.-..', '-..']

for idx, letter in enumerate(hello_world):
    print(morse_code[idx], letter)
    for signal in morse_code[idx]:
        if signal == ' ':
            time.sleep(0.8)
            break
        GPIO.output(18, GPIO.HIGH)
        if signal == '.':
            time.sleep(0.2)
        else:
            time.sleep(0.6)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.2)
    time.sleep(0.6)

print('Hello World!')
