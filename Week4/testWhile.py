# testWhile.py
# basic examples of counter controlled loop and sentinel controlled loop
# Author: Andrea Cignoni

# counter controlled loop

count = 0
while (count < 10):
    print("count is ", count)
    count= count + 1

print ("at the end count is ", count)

count = 10
while count >=0:
    print ("countdown ", count)
    count -= 1
print("blast off")

# sentinel controlled loop

val = input("type something (q to quit):")
while val != "q":
    print ("hi mom")
    val = input("q to quit:")

print ("all done")