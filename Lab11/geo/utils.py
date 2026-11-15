import math

# Return the length of the hypotenuse using the Pythagorean theorem
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Return the area of a circle with radius r
def circle(r):
    area = math.pi * r**2
    return area