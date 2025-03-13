#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

void main()
{
    //acentuacao
    setlocale(LC_ALL, "");

    //cria a variaveis de notas
    float a, b;

    //print para digitar os dois valores
    printf("Digite dois valores para saber a media deles:\n");

    //valores do teclado
    scanf("%f %f",&a,&b);

    //resultado
    printf("A media do valor %f e %f = %f",a,b,(a+b)/2);
}
