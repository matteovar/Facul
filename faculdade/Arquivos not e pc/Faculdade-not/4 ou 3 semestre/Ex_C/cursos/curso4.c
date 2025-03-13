#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main()
{
    //acentuacao
    setlocale(LC_ALL, "");

    //define a variavel
    int a =5;
    float b = 2.5;
    char c = 'c';
    int opcao1 = 1;
    int opcao2 = 2;


    //condicional simples
    if (a=5){
        printf("A variavel a = 5\n");
    }
    if (b = 2.5){
        printf("A variavel b = 2,5\n");
    }
    if (c='c'){
        printf("A variavel c = c\n");
    }
    //numeros par ou impar
    if (a%2 == 0){
        printf("A variavel a 'e par\n");
    }else{
        printf("A variavel 'e impar\n");
    }

    //condicional composta
    if (opcao1==1){
        printf("Opcao 1 aceita");
    }else if (opcao2 == 2){
        printf("Opcao 2 aceita");
    }else{
        printf("Nem opcao 1 e nem opcao 2");
    }

}
