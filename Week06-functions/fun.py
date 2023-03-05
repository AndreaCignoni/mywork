# fun.py
# program showing how lists, tuples and dicts
# can have variables of type function in them
# Author: Andrea Cignoni

def fun1 ():
    print ("this is fun1")
def fun2 ():
    print ("this is fun2")

whichFun = fun1
whichFun ()
whichFun = fun2
whichFun ()