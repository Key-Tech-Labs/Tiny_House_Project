"""Module to test proper LED hardware configuration on Raspberry Pi 3."""

import RPi.GPIO as GPIO
import time
import sys


# Configuration for RPi GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

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
        '?': '..--..',
        '\'': '.----.'
        }


def parse_message(message):
    """Function used to validate given string before passing it to the
    speak_morse_code function. Returns new string void of all characters that
    are not a-z, A-Z, 0-9, or punctuation marks outside of commas, periods,
    apostrophes, and question marks."""

    newly_parsed_message = []

    for letter in message:
        if letter.isalpha() or letter.isdigit() or letter in '.,?\' ':
            newly_parsed_message.append(letter)

    return ''.join(newly_parsed_message)


def speak_morse_code(message):
    """Function which uses the LED light connected to the Raspberry Pi to speak
    (flash) and print the Morse Code translation of the given string."""

    for idx, letter in enumerate(message):
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


if __name__ == '__main__':

    unparsed_message = sys.argv[1]
    parsed_message = parse_message(unparsed_message)
    speak_morse_code(parsed_message)
