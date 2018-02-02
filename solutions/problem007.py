"""
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

max_prime = 10001


# initializing stuff
primes = [2]
i = 3

while len(primes) < max_prime:
    isprime = True

    for prime in primes:
        if i%prime == 0:
            isprime = False
            break
    
    if isprime:
        primes.append(i)

    i += 1

#print(primes)
print(max(primes))
# 104743