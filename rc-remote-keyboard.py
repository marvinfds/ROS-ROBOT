# CamJam EduKit 3 - Robotics
# Controlling the motors with keyboard input

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the CamJam GPIO Zero Library
import RPi.GPIO as GPIO # Import the GPIO Library
import sys, termios, tty, os
robot = CamJamKitRobot()

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.3
rightmotorspeed = 0.3

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


PIN_LED = 25
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, 0)
button_delay = 0.2

for x in range(0, 3):
    GPIO.output(PIN_LED, 1)
    time.sleep(0.25)
    GPIO.output(PIN_LED, 0)
    time.sleep(0.25)

while True:
    char = getch()

    if (char == "q"):
        robot.stop()
        exit(0)

    if (char == "a"):
        print('Left pressed')
        robot.value = motorleft
        time.sleep(button_delay)

    if (char == "d"):
        print('Right pressed')
        robot.value = motorright
        time.sleep(button_delay)

    elif (char == "w"):
        print('Up pressed')
        robot.value = motorforward
        time.sleep(button_delay)

    elif (char == "s"):
        print('Down pressed')
        robot.value = motorbackward
        time.sleep(button_delay)

    robot.stop()

