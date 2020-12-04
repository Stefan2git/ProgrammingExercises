# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Problem taken from: https://projecteuler.net/problem=4

def palindrom():

    array = []

    for i in range(100,1000):
        for x in range(100,1000):
            number = x * i

            if str(number) == str(number)[::-1]:
                array.append(number)

    array.sort()
    return array[-1]

print(palindrom())

# Answer: 906609
