"""
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_py_trip(c_max=1000):
    py_trip = []
    for c in range(0,c_max):
        for b in range(0,c):
            for a in range(0,b):
                if check_py_trip(a,b,c):
                    if a+b+c == c_max:
                        print(a,b,c)
                        py_trip = [a,b,c]
                        return py_trip

    return py_trip

def check_py_trip(a,b,c):
    return (a < b) and (b < c) and (a**2 + b**2 == c**2)

py_trip = find_py_trip()
print(py_trip)
# [200, 375, 425]

print(py_trip[0] * py_trip[1] * py_trip[2])

