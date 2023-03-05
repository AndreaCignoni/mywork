# testIf.py
# else:
#   statements(if else)

# if condition1:
#   statement(if true)
# elif condition2:
# statements(if condition1 is false but 2 is true)
# else:
#   statements(if both false)

# Author: Andrea Cignoni
b =1
if True:
    print("we are in the if statement")
    b=22

c = 1
if c == 1:
    print ("c is one")
else:
    print ("c is not one")

d = "string"
if not isinstance(d, int):
    print("please give me an int")
elif d < 0:
    print ("d is negative")
elif d >= 10:
    print ("d is 10 or higher")
else:
    print ("d is between 2 and 9(inclusive)")
print ("sanity", b)