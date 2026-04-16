"""Copyright (c) 2026 MTHS All rights reserved
Created by: Jayden Okafor
Created on: Apr 2026
This program creates a circle loop using the sprite engine
"""

from MicroPython.microbit import *

# variables
sides = 0
steps = 0
x = 0
y = 0
direction = 0

# show happy face
display.clear()
display.show(Image.HAPPY)

# when button "A" is pressed
while True:
    if button_a.was_pressed():
        # create the sprite at the beginning and wait for 0.1 seconds
        display.clear()
        x = 0
        y = 0
        sides = 0
        direction = 0
        display.set_pixel(x, y, 9)
        sleep(100)

        # if its not back to the position it started then continue code
        while sides < 4:
            # reset the steps to 0 so the sprite can move to the 4th coordinate before stopping
            steps = 0
            # if its not in the last pixel then move 1 step forward and wait for 0.1 seconds
            while steps < 4:
                display.clear()
                if direction == 0:
                    x += 1
                elif direction == 1:
                    y += 1
                elif direction == 2:
                    x -= 1
                elif direction == 3:
                    y -= 1
                display.set_pixel(x, y, 9)
                sleep(100)
                steps += 1
            # turn right when it reaches the end
            direction = (direction + 1) % 4
            sides += 1

        # delete sprite and show happy face
        display.clear()
        display.show(Image.HAPPY)

    # when button "B" is pressed
    if button_b.was_pressed():
        # create the sprite at the beginning and wait for 0.1 seconds
        display.clear()
        x = 0
        y = 0
        sides = 0
        steps = 0
        direction = 0
        display.set_pixel(x, y, 9)
        sleep(100)

        # if its not back to the position it started then continue code
        while sides < 4:
            # reset the steps to 0 so the sprite can move to the 4th coordinate before stopping
            steps = 0
            # if its not in the last pixel then move 1 step forward and wait for 0.1 seconds
            while steps < 4:
                display.clear()
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                elif direction == 3:
                    x -= 1
                display.set_pixel(x, y, 9)
                sleep(100)
                steps += 1
            # turn left when it reaches the end
            direction = (direction + 1) % 4
            sides += 1

        # delete sprite and show happy face
        display.clear()
        display.show(Image.HAPPY)
