#include <stdio.h>
#include <stdlib.h>

void main()
{
    int a =5, b = 10, c =15;

    //maior
    if (a>2){
        printf("%d eh maior que 2\n",a);
    }
    //maior ou igual
    if (c>=b){
        printf("%d eh maior ou igual a %d\n",c,b);
    }
    //menor
    if (a<10){
        printf("%d eh menor que 10\n",a);
    }
    //menor ou igual
    if(b<=10){
        printf("%d eh menor ou igual a 10\n",b);
    }
    //diferente de
    if (a!=10){
        printf("%d eh diferente de 10\n",a);
    }
    //pausa o sistema
    system("pause");
}
