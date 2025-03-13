#include<stdio.h>
#include<stdlib.h>

//funcao principal do programa
void main()
{
    //variaveis
    int a =6, b=3;

    //printa a soma
    printf("A soma de %d + %d = %d\n",a,b,a+b);

    //printa a subtracao
    printf("A subtracao de %d - %d = %d\n",a,b,a-b);

    //printa a divisao
    printf("A divisao de %d / %d = %d\n",a,b,a/b);

    //printa multiplicacao
    printf("A multiplicacao de %d * %d = %d\n",a,b,a*b);

    //printa o resto da divisao
    printf("O resto da divisao de %d e %d = %d\n",a,b,a%b);

    //valor absoluto
    printf("o valor absoluto de -3 = %d\n", abs(-3));

    //pausa o codigo
    system("Pause");


}
