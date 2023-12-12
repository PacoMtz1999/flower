'''from turtle import * 
import colorsys

speed(0)
bgcolor("black")
h=0

for i in range(16):
    for j in range(18):
        c=colorsys.hsv_to_rgb(h,0.9,1)
        color(c)
        h+=0.005
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
    circle(40,24)

done()


from turtle import *
import colorsys

speed(0)
bgcolor("black")

# Set base color as morado
h = 0.5

for i in range(10):
    for j in range(12):
        # Calculate the color based on hue and brightness
        c = colorsys.hsv_to_rgb(h, 0.9, 1)
        # Use a golden color for specific petals
        if i == 0 or i == 3:
            c = (0.8, 0.6, 0.5)
        color(c)

        # Update hue for color variation
        h += 0.005

        rt(90)
        circle(120 - j * 6, 90)
        lt(90)
        circle(120 - j * 6, 90)
        rt(180)

    circle(40, 24)

done()

from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 1.0

for i in range(10):
    for j in range(12):
        # Use modulo operator to determine petal color
        if i % 2 == 0:
            # Set color to purple
            c = colorsys.hsv_to_rgb(0.5, 0.9, 1)
        else:
            # Set color to gold
            c = (0.8, 0.6, 0.5)
        color(c)
        h += 0.005
        rt(90)
        circle(120 - j * 6, 90)
        lt(90)
        circle(120 - j * 6, 90)
        rt(180)
    circle(40, 24)

done()'''

from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 1.0

for i in range(10):
    for j in range(12):
        # Set color based on petal position
        if i < 5:
            c = colorsys.hsv_to_rgb(0.5, 0.9, 1)  # Purple
        else:
            c = (0.8, 0.6, 0.5)  # Gold
        color(c)
        h += 0.005
        rt(90)
        circle(120 - j * 6, 90)
        lt(90)
        circle(120 - j * 6, 90)
        rt(180)
    circle(40, 24)

done()
