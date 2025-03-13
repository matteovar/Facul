#include <stdio.h>
#include <stdlib.h>

int main(void){

    int vetor[3] = {3,1,5}, cont;

     printf("vetor original: ", vetor[cont]);

    //imprime os valores do vetor original
    for (cont = 0;cont<3;cont++){
    printf("%d ", vetor[cont]);
    }
    //adiciona mais 1 nos valores do vetor
    for (cont = 0; cont<3;cont++){
        vetor[cont]= vetor[cont] + 1;
    }
    //imprimir os valores no vetor
    printf("\nvetor modificado: ", vetor[cont]);
    for (cont = 0;cont<3;cont++){
    printf("%d", vetor[cont]);
     }

    for(cont = 0;cont<3;cont++){
        scanf("%d", &vetor[cont] );
     }
    printf("vetor modificado 2 : ", vetor[cont]);
    for (cont = 0;cont<3;cont++){
     }
        printf("%d \n", vetor[cont]);
}
