#include <stdio.h>
#include <stdlib.h>

int main(void){

    //quantidade de strgs possiveis para digitar
        char palavras[255

        //pedi para o usuario digitar
        printf("escreva algo");

    //limpa o buffer
        setbuf(stdin, 0);

    //le os valores digitados
        fgets(palavras, 255, stdin);

    //limpa as casas vazias
        palavras[strlen(palavras)-1] = '\0';

    //printa as palavras digitadas
        printf("%s",palavras);

}
