# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Problem taken from: https://projecteuler.net/problem=1

def multiplesOf3and5(n,m):
    summe = 0

    for i in range(n, m):
        if (i % 3) == 0 or (i % 5) == 0:
            summe += i

    return summe

print(multiplesOf3and5(1, 1000))
