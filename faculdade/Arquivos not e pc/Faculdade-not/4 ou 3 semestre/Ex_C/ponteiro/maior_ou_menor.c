#include <stdio.h>
#include <stdlib.h>

int maioroumenor(int *vetor, int *maior,int *menor, int tamanho){
    *maior = vetor[0];
    *menor  = vetor[0];

    for (int i = 1;i< tamanho; i++){
        if(vetor[i]>*maior){
            *maior = vetor[i];

        }
        if (vetor[i]<*menor){
            *menor = vetor[i];
        }

    }

}

int main(void){
    int vetor [] = {1,2,5,4,8,3};
    int tamanho = sizeof(vetor)/sizeof(int );
    int maior, menor;

    maioroumenor(vetor,&maior,&menor,tamanho);

    printf("Maior numero = %d\n", maior);
    printf("Menor numero = %d", menor);
}
