# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
# Project taken from: https://projecteuler.net/problem=10


def siebDesEratosthenes(n):

    numbers = []
    for i in range(n+1):
        numbers.append(True)

    numbers[0] = False
    numbers[1] = False
    position = 2

    while position ** 2  < (n+1):

        if numbers[position] == True:
            for i in range(position*2, n+1, position):
                numbers[i] = False

        position += 1

    primzahlen = []
    for i in range(n+1):
        if numbers[i] == True:
            primzahlen.append(i)

    return primzahlen


def summePrimes(n):
    summe = sum(siebDesEratosthenes(n))
    return summe

print(summePrimes(2000000))

#Antwort = 142913828922

