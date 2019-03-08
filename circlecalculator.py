# Created by: Aden Rao
# Created on: March 2nd, 2019 
# This program you put in the diameter of a circle and it will calculate the area and circumference of the circle.

# Input for the user to put the diameter in

diameter = int(input( ' enter the diameter: '))

# Math calculations and formulas

import math

circumference = 2 * (math.pi * (diameter/2))
area = math.pi * (diameter/2) ** 2 
print( "The circumference is " + str(circumference))
print( "The area is " + str(area))

# Prints than you

end = input ('Thank You!')
