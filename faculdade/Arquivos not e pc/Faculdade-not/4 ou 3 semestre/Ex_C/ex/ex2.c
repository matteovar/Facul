#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

void main()
{
    //acentuacao
    setlocale(LC_ALL, "");

    //cria a variaveis de notas
    int a, b;

    //print para digitar os dois valores
    printf("Digite dois valores para saber a media deles:\n");

    //valores do teclado
    scanf("%d %d",&a,&b);

    //final
    printf("O valor absoluto de %d - %d = %d",a,b,abs(a-b));
}
