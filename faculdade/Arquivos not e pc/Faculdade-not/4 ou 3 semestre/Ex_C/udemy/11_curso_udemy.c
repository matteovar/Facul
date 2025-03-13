#include <stdio.h>
#include <stdlib.h>

int main(void){
    int vetor[3]={5,6,7}, cont, media = 0;

    for (cont = 0; cont<3;cont++){
        scanf("%d", &vetor[cont]);
        media += vetor[cont];
    }
    for (cont = 0;cont<3;cont++){
        printf("valor do vetor na posicao %d = %d\n",cont, vetor[cont]);

    }

    media  /= 3;
    printf("%d", media);
}
