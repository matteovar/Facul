#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void main(){

    //definindo as variaveis
    bool a = true, b = false;

    //se A for verdadeiro
    if (a){
        printf("A eh verdade\n");
    }

     //se B for falso
     if (b){
        printf("B eh verdadeiro\n");
     }else{
        printf("B eh falso\n");
     }

     //comprando uma falsidade
     if(!b){
        printf("B eh falso\n");
     }

}
