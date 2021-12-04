// because i hate myself
// Peter Derias

#include <stdio.h>
#include <stdlib.h>

#define SIZE 12
#define INPUT_SIZE 1000
// assume that the file is open, and is of the correct format.
// causes a leak if you dont free both the inside and the outside.
char **read2DArrayFromFile(FILE *file) {
    char **array = malloc(INPUT_SIZE * sizeof(char *));
    for (int i = 0; i < INPUT_SIZE; i++) {
        array[i] = malloc(SIZE + 2);
        fgets(array[i], SIZE + 2, file);
    }
    return array;
}

// these two should be one function with pointer shit but i cant be bothered.
char getMostCommonCharInLine(int i, char** array) {
    int num1 = 0;
    int num0 = 0;
    for (int j = 0; j < INPUT_SIZE; j++) {
        if (array[j][i] == '0') num0++;
        else num1++;
    }
    return (num0 > num1) ? '0': '1';
}

int getNumberOfCharInLine(int i, char c, char ** array) {
    int num = 0;
    for (int j = 0; j < INPUT_SIZE; j++) {
        if (array[j][i] == c) num++;
    }
    return num;
}

// get the gamma given an array. This causes a leak if you dont free.
char *getGamma(char **array){
    char *gamma = malloc(SIZE);
    for (int i = 0; i < SIZE; i++) {
        gamma[i] = getMostCommonCharInLine(i, array);
    }
    return gamma;
}

void getQ1(char **array) {
    char *gamma = getGamma(array);
    int gammaNum = (int) strtol(gamma, NULL, 2);
    int epsilonNum = ~gammaNum & ((1 << SIZE) - 1);
    printf("Q1: %d\n", gammaNum * epsilonNum);
}

int main (void) {
    FILE *file = fopen("./input.in", "r");
    // i should check but im lazy
    char **array = read2DArrayFromFile(file);
    getQ1(array);
    // would rather die than do q2 in C
    // freeing is for nerds
    return 0;
}
