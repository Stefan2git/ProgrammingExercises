#include <stdio.h>
#include <string.h>

/*
 * Returns the number of letters as an integer for a number below 100
 */
int underHundred(int i)
{
    char  digits[][10] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                          "eleven","twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                          "eighteen", "nineteen"};
    char tens[][10] = {"zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    int counter = 0;

    /* numbers between 0 and 19 (inclusive) */
    if (i < 20) {

        if (i == 0){
            return 0;
        }

        if (i < 10) {
            printf("%s\n", digits[i]);
            counter = strlen(digits[i]);
            return counter;

        } else if (i == 10) {
            printf("%s\n", tens[1]);
            counter = strlen(tens[1]);
            return counter;

        } else if (11 < i < 20) {
            printf("%s\n", digits[i-1]);
            counter = strlen(digits[i-1]);
            return counter;
        }
    }

    /* Numbers between 20 and 99 (inclusive) */
    if (i >= 20){

        /* numbers bigger than 19 and divisible by 10 without remainder
         * for eg. 20, 30, 40,..., 90
         */
        if (i % 10 == 0){
            int tmp = i / 10;
            printf("%s\n", tens[tmp]);
            counter = strlen(tens[tmp]);
            return counter;
        }

        /*for all numbers that are above 20 and are not 20,30,40,..90
         * for eg. 21,22,23,...,98,99
         */
        else {
            /* calculates the first digit */
            int first = i / 10;

            /*calculates the second digit */
            int zehnerstelle = first * 10;
            int rest = i % zehnerstelle;

            counter += strlen(tens[first]);
            counter += strlen(digits[rest]);

            printf("%s-", tens[first]);
            printf("%s\n", digits[rest]);

            return counter;

        }
    }
    return 0;
}


/*
 * Returns the number of letters as an integer for a number between 100 and 999 (inclusive)
 */
int overHundred(int i)
{
    char  digits[][10] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int counter = 0;

    /* calculates the first digit */
    int hundred = i / 100;

    counter += strlen(digits[hundred]);
    counter += strlen("hundred");

    printf("%s hundred", digits[hundred]);

    /* if number is full hundert (100,200,300,...900) no "and" will be counted */
    if (i % 100 != 0) {
        counter += strlen("and");
        printf(" and ");
    }
    else{
        printf("\n");
    }

    /* calculates the second and third digit of the number */
    int tmp1 = hundred * 100;
    int tmp = i - tmp1;

    counter += underHundred(tmp);

    return counter;
}


/*
 * Retruns the length of string "one-thousand" to counter
 */
int oneThousand()
{
    int counter;
    counter = strlen("onethousand");
    return counter;
}
