#include <stdio.h>

int collatz(int b){

    int counter = 1;
    long long n = b;

    do {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = (3 * n) + 1;
        }
        counter += 1;
    } while (n > 1);

    return counter;
}


void schleife(int n){

    int highest_zahl = 0;
    int highest_count = 0;

    for (int i = 1; i <= n; i++){

        int counter = collatz(i);

        if (counter > highest_count){
            highest_count = counter;
            highest_zahl = i;
        }
    }
    printf("Zahl = %d\n", highest_zahl);
    printf("Counter = %d\n", highest_count);


}


int main(){

    int a = 1000000;
    schleife(a);

    return 0;
}

//Antwort:
//Zahl = 837799
//Counter = 525