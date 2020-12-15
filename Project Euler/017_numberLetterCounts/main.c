#include <stdio.h>
#include "counter.h"


/*
 * If the numbers 1 to 5 are written out in words: one, two, three,
 * four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 *
 * This programm calculates the number of letters for the numbers 1 to 1000 (inclusive)
 *
 */
int main()
{
    int counter = 0;

    /* Adds up the string length of numbers between 1 and 999 */
    for (int i = 1; i < 1001; i++){
        if (i < 100)
            counter += underHundred(i);
        else if(i == 1000)
            counter += oneThousand();
        else if(i >= 100)
            counter += overHundred(i);
        }

    printf("Letter count: %d", counter);

    return 0;
}

// Answer: 21124
