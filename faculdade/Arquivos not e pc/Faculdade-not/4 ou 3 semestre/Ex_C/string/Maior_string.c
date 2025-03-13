#include <stdio.h>
#include <stdlib.h>

int main(void){
    char vet1[255], vet2[255], vet3[255];
    char maior[255];

    printf ("Digite a primeiro string");
    scanf("%s", vet1)

    printf ("Digite a segunda string");
    scanf("%s", vet2)

    printf ("Digite a terceira string");
    scanf("%s", vet3)

    if (strcmp(vet1, vetor2)<0){
        maior = vetor2;
    }   
    if (strcmp(vetor1,vetor3)<0){
        maior = vetor3;
    }

    printf("A string lexicograficamente maior é: %s\n", max);

    return 0;
}