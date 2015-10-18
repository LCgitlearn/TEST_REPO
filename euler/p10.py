from math import sqrt
primes = []
def checkPrime(num):
    maxLoop = sqrt(num)
    for i in primes:
        if i > maxLoop:
            return True
        if num%i == 0:
            return False
    return True

for i in xrange(2, 2000000):
    if(checkPrime(i)):
        primes.append(i)
print sum(primes)
