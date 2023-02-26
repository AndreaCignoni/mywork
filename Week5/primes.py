# generate primes
# Author: Andrea Cignoni

primes = []
upto = 10001

for candidate in range(2, upto):
    # print (candidate)
    isPrime = True
    # only check if divisable by primw
    for divisor in range(2, candidate):
        # if divisable by an int is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no reason for checking
            break

    if isPrime:
        primes.append (candidate)

print (primes)