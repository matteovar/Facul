#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int obter_maior(int v[], int n){
    int maior = v[0];
    for (int i = 1; i<n;i++){
        if (v[i]>maior){
            maior = v[i];
        }
    }
    return maior;
}

int obter_menor(int v[], int n){
    int menor = v[0];
    for (int i = 1; i < n ;i++){
        if (v[i]< menor){
            menor = v[i];
        }
    }
    return menor;
}

int obter_pares(int v[], int n){
    int cont = 0;
    for (int i = 1; i<n; i++){
        if (v[i]%2 == 0){
            cont++;
        }
    }
    return cont;
}

float media_valores(int v[], int n){
    int soma = 0;
    for (int i = 0; i<n;i++){
        soma += v[i];
    }
    return ((float)soma/n);
}

float media_valores2(int v[], int n, float media){
   for(int i = 0; i<n; i++){
    if(v[i]<media)
        printf("%d ", v[i]);

   }
   printf("\n");
}




void main(){
    int v[5]={55,24,99,10,25};
    int n = 5;
    printf("Maior elemento do vetor: %d\n", obter_maior(v, n));

    printf("Menor elemento do vetor: %d\n", obter_menor(v,n));

    printf("A quantidade de numeros pares no vetor 'e: %d\n", obter_pares(v, n));

    float media = media_valores(v,n);

    printf("A media entre os valores: %.1f\n", media);

    media_valores2(v,n,media);

    return 0;

}
