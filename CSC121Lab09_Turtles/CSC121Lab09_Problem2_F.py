__author__ = 'Michele Johnson'
# Program Requirements
# Write a Python program that uses Turtle Graphics to draw the letter “F” with three lines.
# Decide the size and the location of the letter yourself.

# Import and setup Turtle
import turtle
display1 = turtle.Screen()
display1.setup(width=800, height=600)
turtle_f = turtle.Turtle()
turtle_f.hideturtle()
turtle_f.pensize(10)
turtle_f.pencolor("red")

# Define Coordinates
coordinate1 = 100
coordinate2 = 275
center = 0

# Draw line 1 of 3
turtle_f.penup()
turtle_f.setposition(-coordinate1, coordinate2)
turtle_f.pendown()
turtle_f.setposition(-coordinate1, center)

# Draw line 2 of 3
turtle_f.penup()
turtle_f.setposition(-coordinate1, coordinate2)
turtle_f.pendown()
turtle_f.setposition(0.60*coordinate1, coordinate2)

# Draw line 3 of 3
turtle_f.penup()
turtle_f.setposition(-coordinate1, 0.60*coordinate2)
turtle_f.pendown()
turtle_f.setposition(center, 0.60*coordinate2)

display1.exitonclick()
