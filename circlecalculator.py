# Created by: Aden Rao
# Created on: March 2nd, 2019 
# This program you put in the diameter of a circle and it will calculate the area and circumference of the circle.

diameter = int(input( ' enter the diameter: '))

import math

circumference = 2 * (math.pi * (diameter/2))
area = math.pi * (diameter/2) ** 2 
print( "The circumference is " + str(circumference))
print( "The area is " + str(area))

end = input ('Thank You!')
