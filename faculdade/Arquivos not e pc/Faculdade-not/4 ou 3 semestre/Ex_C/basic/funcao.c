//definir o tamanho da variavel pelo codigo inteiro

#include <stdio.h>
#include <stdlib.h>
#define TAM  10//defini o tamanho da variavel como 10 para o codigo inteiro

int main(void){

    printf("%d\n", TAM);

    for (int i = 0; i<=TAM; i++){
        printf("%d ", i);
    }
}
