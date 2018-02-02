"""
Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# imports
import numpy as np

max = 100

# Create a list of 1 to 100
i = np.arange(1,max+1,1)

sum_of_squares = sum([x**2 for x in i])
square_of_sum = sum([x for x in i])**2

#print(sum_of_squares)
#print(square_of_sum)

print(square_of_sum-sum_of_squares)
# 25164150