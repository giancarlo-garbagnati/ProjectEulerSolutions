"""
Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Recursive solution, finds the lowest divisible number between the current number and the previous
# lowest divisble
def lowest_divisible(x):
    if x == 1:
        return 1
    else:
        y = lowest_divisible(x-1)
        z = y
        while z%x!=0:
            z += y
    return z

print(lowest_divisible(20))
# 232792560