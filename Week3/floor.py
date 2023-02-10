# floor.py
# This program takes in a float and outputs an int rounded down
# Author: Andrea Cignoni
import math

numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))