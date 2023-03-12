# Messing With Files 2
# Creating a file called "count.txt" outside of memory

FILENAME = "count.txt"
"""
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
num = readNumber ()
print (num)
# This program does not seem to work
"""
# Writing a function that takes in a number
# and overwrites a file with that number (count.txt)
""""
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# tested it and this time it worked
writeNumber (3)
"""
# This program uses two functions (readNumber and writeNumber)
# to count how many times it has been run

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

# main
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber (num)