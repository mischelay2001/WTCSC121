__author__ = 'Michele Johnson'
# Program Requirements
# # Write a Python program that shows a turtle walking back and forth between two vertical walls.  
# Please do the following:
# (a)	Create a 800 X 600 Turtle Graphics window
# (b)	Draw a vertical line at x-coordinate = -300.  
# The y-coordinates of the two end points are 200 and -200, respectively.
# (c)	Draw another vertical line at x-coordinate = 300.  
# The y-coordinates of the two end points are 200 and -200, respectively.
# (d)	Create a turtle object and change the shape from arrowhead to turtle.
# (e)	Use a loop to make the turtle walk 2000 steps.  
# Whenever the turtle hits a wall, it turns 180 degree and continues to walk.

# Import and setup turtle
# Define screen size, pen size and color
import turtle
display1 = turtle.Screen()
display1.setup(width=800, height=600)
turtle_wall = turtle.Turtle()
turtle_wall.shape("turtle")
turtle_wall.pensize(10)

# Define coordinate limits
position_x = 300
position_y = 200

# Draw vertical walls: left and right
# Left wall
turtle_wall.penup()
turtle_wall.setposition(-position_x, position_y)
turtle_wall.pendown()
turtle_wall.setposition(-position_x, -position_y)

# Right wall
turtle_wall.penup()
turtle_wall.setposition(position_x, position_y)
turtle_wall.pendown()
turtle_wall.setposition(position_x, -position_y)

# Reposition turtle before it walks between walls
# Change pen size and color
position_x = -282
position_y = 0
turtle_wall.pensize(6)
turtle_wall.pencolor("orange")
turtle_wall.penup()
turtle_wall.setposition(position_x, position_y)
turtle_wall.pendown()

# Loop repeats until turtle has taken 2000 steps
# If nose of turtle touches a wall (absolute value of x-coordinate 282),
# it turns around and goes in opposite direction
for i in range(2000):
    turtle_wall.forward(1)
    if turtle_wall.xcor() <= position_x:
        turtle_wall.left(180)
    elif turtle_wall.xcor() >= -position_x:
        turtle_wall.right(180)

display1.exitonclick()
