#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void contador(char *str) {
    int vet1[256] = {};
    
    for (int i = 0; i < strlen(str); i++) {
        vet1[(int)str[i]]++;
    }

    printf("Letra   Quantidade\n");
    for (int i = 0; i < 256; i++) {
        if (vet1[i] > 0) {
            printf(" %c    -     %d\n", (char)i, vet1[i]);
        }
    }
}


int main() {
    char str[]="banana";

    contador(str);
    
    return 0;
}
