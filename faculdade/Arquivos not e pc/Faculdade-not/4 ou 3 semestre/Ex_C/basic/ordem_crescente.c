#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool orderm_crescente(int v[], int n){
    for (int i =1; i<n;i++){
        if (v[i-1]<v[i])
            return 1;
    return 0;
    }
}

void main(){
    int v[5]={1,2,3,4,5};
    int n = 5;
    printf("Esta em ordem crescente: %s", orderm_crescente(v,n) ?"Sim\n" : "Nao\n");

    return 0;
}
