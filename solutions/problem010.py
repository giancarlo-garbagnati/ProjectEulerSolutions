"""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

max = int(2e6)

# Took about 15 min...
def find_all_primes(max=max):
    primes = []
    for i in range(2,max):
        prime = True
        for j in range(0,len(primes)):
            if i%primes[j] == 0:
                prime = False
                break
        if prime:
            primes.append(i)
            
    return primes

primes = find_all_primes()
print(sum(primes))
# 
