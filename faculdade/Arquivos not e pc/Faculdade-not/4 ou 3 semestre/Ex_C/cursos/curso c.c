#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
/*
int main()
{
 printf("Bom dia, primeiro teste");

}
*/


int main()
{
    //permite usar acento
    setlocale(LC_ALL,"");

    //imprime Olá
    printf("Olá\n");
    //numero inteiro
    int a = 15848;
    printf("o valor de a = %d\n",a);
    scanf("%d",&a);
    printf("O valor de a mudou para %d\n",a);
    //numero em decimal
    float b = 152.25;
    printf("o valor de B é:%f\n",b);
    scanf("%f", &b);
    printf("o valor de B mudou para %f\n",b);
    //letra
    char letra='t';
    printf("O valor de c é = %c\n ",letra);
    fflush(stdin);
    scanf("%c\n", &letra);
    printf("O valor de c mudou para %c\n", letra);
}

// imprime oi galera
//printf("oi galera);

//escrever o valor de uma variavel:
//printf("%d",a);

//escrer um texto com variavel
//printf("O valor de a = %d", a);

//escrever um testo e pular linha(\n)
//prinf("Oi galera!\Aqui estou mais um dia, sobre o olhar sanguinario do vigia.")




