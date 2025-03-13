#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void maior(char vet1[], char vet2[],char vet3[]){

    char maior_string[50];
    strcpy(maior_string,vet1);

    if (strcmp(vet2,maior_string)>0){
        strcpy(maior_string,vet2);
    }
    if (strcmp(vet3,maior_string)>0){
        strcpy(maior_string,maior_string);
    }
        
}
int main(){
    char maior_string[50];
    char vet1[] = "b";
    char vet2[] = "a";
    char vet3[] = "c";
    maior(vet1,vet2,vet3);
    printf("A maior string foi: %s",maior_string);
    return 0;

}
