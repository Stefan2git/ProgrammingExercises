# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# Problem taken from: https://projecteuler.net/problem=3


def largestPrimeFactor(n):
    i = 2
    primfaktoren = []

    while i <= n:
        if n % i == 0:
            primfaktoren.append(i)
            n = n / i
        else:
            i += 1

    return primfaktoren[-1]

print(largestPrimeFactor(600851475143))

#Ansert: 6857

