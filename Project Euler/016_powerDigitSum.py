# Power digit sum
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?
#
#Problem taken from: https://projecteuler.net/problem=16


def sumDigits():
    n = 2 ** 1000
    sum = 0

    for i in str(n):
        sum += int(i)

    return sum

print(sumDigits())

#Answer: 1366 
