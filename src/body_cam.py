"""Module which holds PiCamera configurations."""

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/rpi_camera_test.jpg')
camera.stop_preview()

