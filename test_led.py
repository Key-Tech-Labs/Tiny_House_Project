"""Module to test proper LED hardware configuration on Raspberry Pi 3."""

import RPi.GPIO as GPIO
import time


# Configuration for RPi GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

hello_world = 'Hello World'

# Dict that holds morse code
morse_code = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..'
        }

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
