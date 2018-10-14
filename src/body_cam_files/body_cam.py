"""Module which holds PiCamera configurations."""

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/Desktop/rpi_recording_test.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

