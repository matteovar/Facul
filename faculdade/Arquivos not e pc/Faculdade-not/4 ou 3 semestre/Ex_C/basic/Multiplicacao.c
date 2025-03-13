#include<stdio.h>
#include<stdlib.h>
#include<locale.h>

void main()
{
    //acentuacao
    setlocale(LC_ALL, "");

    //cria variaveis
    int a,b,c;

    //print para oque o usuario deve fazer
    printf("Digite 3 numeros para uma multiplicacao");

    //tecla do usuario
    scanf("%d %d %d",&a,&b,&c);

    //printa para o resultado
    printf("A multiplicacao de %d x %d x %d = %d",a,b,c,a*b*c);

}
