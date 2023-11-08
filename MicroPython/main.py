"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
import robotbit

# variables
servo_number_1 = robotbit.servo(1, 0)

# set up
display.show(Image.HAPPY)

# when button a is pressed, turns servo to 0 degrees.
while True:
    if button_a.is_pressed():
        robotbit.servo(1, 0)
        display.clear()
        print("0")
        display.show(Image.SQUARE_SMALL)
        display.clear()
        display.show(Image.HAPPY)

    # when button b is pressed, turns servo to 180 degrees.
    if button_b.is_pressed():
        robotbit.servo(1, 180)
        display.clear()
        print("180")
        display.show(Image.SQUARE_SMALL)
        display.clear()
        display.show(Image.HAPPY)
