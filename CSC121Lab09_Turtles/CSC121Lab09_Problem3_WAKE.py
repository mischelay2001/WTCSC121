__author__ = 'Michele Johnson'
# Program Requirements
# Write a Python program that uses Turtle Graphics to draw the word “WAKE”.
# Decide the size and the location of the letters yourself.

# Import and setup turtle
# Define screen size, pen size and color
import turtle
display1 = turtle.Screen()
display1.setup(width=800, height=600)
turtle_wake = turtle.Turtle()
turtle_wake.hideturtle()
turtle_wake.pensize(15)
turtle_wake.pencolor("blue")

# Define Coordinates
center = 0
# Define width and height in units for simpler arithmetic
width_x = 800/32
height_y = 300/12

# Write W
# Set left-most x coordinate position
position_x = -350
# Draw line 1 of 4: top-left to bottom-left
turtle_wake.penup()
turtle_wake.setposition(position_x, height_y*11)
turtle_wake.pendown()
turtle_wake.setposition(position_x, center)
# Draw line 2 of 4: bottom-left to horizontal-center/vertical-70%
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*3, height_y*7)
# Draw line 3 of 4: horizontal-center/vertical-70% to bottom-right
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, center)
# Draw line 4 of 4: bottom-right to top-right
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, height_y*11)

# Write A
# Set left-most x coordinate position
position_x = -163
# Draw line 1 of 3: bottom-left to horizontal-center/vertical-top
turtle_wake.penup()
turtle_wake.setposition(position_x, center)
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*3, height_y*11)
# Draw line 2 of 3: horizontal-center/vertical-top to bottom-right
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, center)
# Draw line 3 of 3: horizontal line between line 1 and 2
turtle_wake.penup()
turtle_wake.setposition(position_x+width_x*1.5, height_y*5)
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*4.5, height_y*5)
#
# Write K
# Set left-most x coordinate position
position_x = 25
# Draw line 1 of 3: bottom-left to top-left
turtle_wake.penup()
turtle_wake.setposition(position_x, center)
turtle_wake.pendown()
turtle_wake.setposition(position_x, height_y*11)
# Draw line 2 of 3: mid-left to top-right
turtle_wake.penup()
turtle_wake.setposition(position_x, height_y*11/2)
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, height_y*11)
# Draw line 3 of 3: mid-left to bottom-right
turtle_wake.penup()
turtle_wake.setposition(position_x, height_y*11/2)
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, center)

# Write E
# Set left-most x coordinate position
position_x = 207
# Draw line 1 of 4: bottom-left to top-left
turtle_wake.penup()
turtle_wake.setposition(position_x, center)
turtle_wake.pendown()
turtle_wake.setposition(position_x, height_y*11)
# Draw line 2 of 4: top-left to top-right
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, height_y*11)
# Draw line 3 of 4: mid-left to mid-right
turtle_wake.penup()
turtle_wake.setposition(position_x, height_y*11/2)
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*4.5, height_y*11/2)
# Draw line 4 of 4: bottom-left to bottom right
turtle_wake.penup()
turtle_wake.setposition(position_x, center)
turtle_wake.pendown()
turtle_wake.setposition(position_x+width_x*6, center)


display1.exitonclick()
