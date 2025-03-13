#include <stdio.h>
#include <stdlib.h>

int main(void){

    //variaveis
    int a = 10;

    //imprimindo a variavel
    printf("variavel a  =  %d\n", a);

    //endereco  da variavel
    printf("escrevendo por cima da variavel %d\n", &a);

    //variaveis qu armazenam o valor
    int b =10;

    int *ponteiros;

    ponteiros = &b;

    printf("imprimindo o valor de b armazenado %d\n", b);

    *ponteiros = 40;

    printf("valor da variavel mudou para %d", b);

    return 0;

}
