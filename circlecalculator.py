# Created by: Aden Rao
# Created on: March 2nd, 2019 
# This program you put in the diameter of a circle and it will calculate the area and circumference of the circle.

diameter = int(input( ' enter the diameter: '))

import math

print (round(math.pi*(diameter/2)*(diameter/2))), print ("Area")
print (round(math.pi*(diameter))), print ("Circumference")
