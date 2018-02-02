"""
Largest palindrome product
Problem 4 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# define some helper fxns

def ispalindrome(s):
    """ Takes a string and returns True if it's a palindrome (and False if not)
    """
    
    i = int(len(s)/2)
    s2 = s

    # if it a number with an odd number of chars, we'll just remove the middle char
    if len(s)%2==1:
        s2 = s[:i] + s[i+1:]
    
    # Check if it's a palindrome
    if s2[:i]==s2[i:][::-1]:
        return True
    else:
        return False


x = 999
y = 999

palindromes = []

while (x > 0) and (y > 0):
    z = x*y
    z_str = str(z)

    # collect all palindromes
    if ispalindrome(z_str):
        if z not in palindromes:
            palindromes.append(z)
    
    y -= 1
    if y < 1:
        x -= 1
        y = x


print(max(palindromes))
# 906609