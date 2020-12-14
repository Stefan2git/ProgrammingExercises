# Lattic Paths
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
#
# Problem taken from: https://projecteuler.net/problem=15


def grid(n):

    array = []

    # Path 1
    array.append(1)

    if n >= 2:

        for i in range(n):
            array.append(1)

        array_tmp = array[:]

        for i in range(1, n-1):
            sum_tmp = 0

            for x in range(n, 0, -1):
                sum_tmp += array[-x]
                array_tmp.append(sum_tmp)

            array = array_tmp[:]

    paths = sum(array) * 2
    return paths

print(grid(20))

# Answer: 137846528820
