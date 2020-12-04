# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Problem taken from: https://projecteuler.net/problem=5


def checkIfPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def divisible(number, n, m):
    for i in range(n, m+1):
        if number % i != 0:
            return False
    return True

def smallest_multiple(n,m):
    divisor = []

    for i in range(n,m+1):
        divisor.append((i))

    # get prime numbers in list of divisors:
    primes = []
    for i in divisor:
        if checkIfPrime(i) == True:
            primes.append(i)

    # get least common multiple of prime numbers
    least_common_multiple = 1
    for i in primes:
        least_common_multiple *= i

    number = least_common_multiple
    while True:
        if divisible(number, n, m) == True:
            return number

        number += least_common_multiple

print(smallest_multiple(1,20))

#Answer: 232792560
