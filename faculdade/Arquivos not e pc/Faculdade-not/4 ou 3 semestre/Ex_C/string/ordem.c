#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ordem(char vet1[], char vet2[], char vet3[]){
    char aux[50];

    if (strcmp(vet1,vet2)>0){
        strcpy(aux,vet1);
        strcpy(vet1,vet2);
        strcpy(vet2,aux);
    }
    if (strcmp(vet1,vet3)>0){
        strcpy(aux,vet1);
        strcpy(vet1,vet3);
        strcpy(vet3,aux);
    }
    if (strcmp(vet2,vet3)>0){
        strcpy(aux,vet2);
        strcpy(vet2,vet3);
        strcpy(vet3,aux);
    }

}

int main(){
    char aux[50];
    char vet1[50] = "c";
    char vet2[50] = "b";
    char vet3[50] = "a";

    ordem(vet1,vet2,vet3);

    printf("As strings em ordem crescente sao: %s %s %s", vet1,vet2,vet3);

    return 0;

}