"""
Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Go through and check every factor
unique_prime_factor = []
prime_factors = []
x = 600851475143
i = 2
while i < x+1:
    if x%i==0:
        prime_factors.append(i)
        if i not in unique_prime_factor:
            unique_prime_factor.append(i)
        x /= i
        i = 2
    else:
        i += 1

print(prime_factors)
print(unique_prime_factor)
# [71, 839, 1471, 6857]
print(max(unique_prime_factor))
# 6857