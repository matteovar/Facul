#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){

    setlocale(LC_ALL, "");

  //cria a variavel
  int a = 30;

  //conectivo logico E(and)
  if (a>5 && a<15){ //and 'e representado por &&
    printf("A variavel esta entre 5 e 10\n");
  }

  //conectivo logico OU (or)
  if (a>5 || a<15){ //Ou 'e representado por &&
    printf("A variavel 'e maior que 5 ou 15'\n");
  }

  //conectivos juntos
  if ((a>15 && a<15) || a==10){
    printf("A variavel 'a' esta entre 5 e 15 ou vale 10");
  }else{
    printf("A variavel nao esta em lugar nenhum");


  }


}
