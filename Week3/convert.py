# convert.py
# This program takes in a float in dollars 
# and outputs an absolute number in cent
# author: Andrea Cignoni

number = float(input("Enter an amount in dollars = $ "))
cent = abs(int(number*100))
print('The amount you have entered is {}'.format(cent))