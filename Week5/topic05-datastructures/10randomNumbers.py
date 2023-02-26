# 10randomNumbers.py
# This program puts 10 random numers into a queue,
# then outputs all the values in the queue,
# then take the numbers from the queue one at a time,
# print it and the current numbers still in the queue
# Author: Andrea Cignoni

import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range (0, numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print (f"queue is {queue}")

while len (queue) != 0:

    currentNumber = queue.pop(0)
    print (f"current Number is {currentNumber} and the queue is {queue}")
# problem with this line was that the f function was not inserted
print ("the queue is now empty")