__author__ = 'Michele Johnson'
# Program Requirements
# Write a Python program that uses Turtle Graphics to draw the letter “W” with four lines.
# Decide the size and the location of the letter yourself.

# Import and setup Turtle
import turtle
display1 = turtle.Screen()
display1.setup(width=800, height=600)
turtle_w = turtle.Turtle()
turtle_w.hideturtle()
turtle_w.pensize(5)
turtle_w.pencolor("green")

# Define Coordinates
coordinate1 = 100
coordinate2 = 275
center = 0

# Draw line 1 of 4
turtle_w.penup()
turtle_w.setposition(-coordinate1, coordinate2)
turtle_w.pendown()
turtle_w.setposition(-0.5 * coordinate1, center)

# Draw line 2 of 4
turtle_w.pendown()
turtle_w.setposition(center, 0.75 * coordinate2)

# Draw line 3 of 4
turtle_w.pendown()
turtle_w.setposition(0.5 * coordinate1, center)

# Draw line 4 of 4
turtle_w.pendown()
turtle_w.setposition(coordinate1, coordinate2)

display1.exitonclick()
