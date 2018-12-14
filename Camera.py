# Camera Code
# Animesh Patel                     12/11/2018

import picamera

from time import sleep
import sys
camera = picamera.PiCamera()

powerOn = 1

# Servo default position: left side
camera_side_current = "left"
camera_side_next = "center"

counter = 1

while powerOn:
    
    if camera_side_current == "left":
        print("picture from left side\n")
        camera_side_next = "center"

    elif camera_side_current == "center":
        print("picture from center side\n")
        camera_side_next = "right"

    elif camera_side_current == "right":
        print("picture from right side\n")
        camera_side_next = "left"

    sleep(.5)
    camera.start_preview()
    sleep(.5)
    camera.stop_preview()


    if camera_side_current == "left":
        camera.capture('/home/pi/Desktop/Pictures/Left_Side_%s.jpg' %counter)

    elif camera_side_current == "center":
        camera.capture('/home/pi/Desktop/Pictures/Center_Side_%s.jpg' %counter)

    elif camera_side_current == "right":
        camera.capture('/home/pi/Desktop/Pictures/Right_Side_%s.jpg' %counter)


    print('done with ' + camera_side_current + ' side\n')
    sleep(1.5)
    camera_side_current = camera_side_next

    if camera_side_current == "left":
        counter = counter + 1
        sleep(2.5)

