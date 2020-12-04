# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
#
# Problem taken from: https://projecteuler.net/problem=7


def primes():

    numbers = [i for i in range(2, 110000)]

    i = 0
    while i < 10000:
        a = i

        while a < len(numbers):
            if numbers[a] % numbers[i] == 0 and numbers[a] != numbers[i]:
                del numbers[a]

            a += 1
        i += 1

    return numbers[i]

print(primes())

#Answer: 104743















