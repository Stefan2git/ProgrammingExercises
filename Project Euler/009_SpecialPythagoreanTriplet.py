# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 2^5 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# Problem taken from: https://projecteuler.net/problem=9

import math

def pythagoreanTriplet():

    for a in range(1, 500):
        for b in range(1, 500):

            c = a**2 + b**2
            c_square_root = math.sqrt(c)

            if (1000 - c_square_root) == (a + b) and a < b < c_square_root:
                print(str(a) + " + " + str(b) + " + " +  str(c_square_root) + " = " + str(a+b+c_square_root))
                return a,b,c_square_root

pythagoreanTriplet()


# Answer:
# a = 200
# b = 375
# c = 425
