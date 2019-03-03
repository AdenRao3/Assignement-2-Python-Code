# Created by: Aden Rao
# Created on: Febuary 2th, 2019 
# This program you put in the diameter of a circle and it will calculate the area and circumference of the circle.

diameter = int(input( ' enter the diameter: '))

import math

print (round(math.pi*(diameter/2)*(diameter/2)))
print (round(math.pi*(diameter)))
