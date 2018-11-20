__author__ = 'Michele Johnson'
#Program requirements:
# Mary is a big fan of tropical fish.  She has a few tanks of fish at home.
# To maintain a healthy environment for the fish, she needs to add conditioner to the water once a week.
# The amount of conditioner added is determined by the volume of water in the tank.
# According to the direction on the bottle, she has to add 1 teaspoon of conditioner per 100 cubic inches of water.
# She wants a program to calculate the amount of conditioner to add to each tank.  All tanks are rectangular.
# The program will ask for the length, width and height of the tank.
# It will calculate and display the amount of conditioner to add. [Note: volume = length * width * height]

#Calculations
length = int(input('Enter length of tank in inches: '))
width = int(input('Enter width of tank in inches: '))
height = int(input('Enter height of tank in inches: '))
volume = length * width * height
Cubic_Volume = volume // 100

#Output
print('\nThe volume of Mary\'s tank is', volume, 'cubic inches. '
      '\nMary would need to add', Cubic_Volume, 'teaspoons of conditioner to her tank.')
