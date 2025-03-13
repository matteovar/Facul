#include <stdio.h>
#include <string.h>

int palindromo(char vet1[]){

    int i,tamanho;

    tamanho = strlen(vet1);

    for(i=0;i<tamanho/2; i++){
        if(vet1[i]!=vet1[tamanho-i-1]){
            return 0;
        }
    }
    return 1;
}

int main(){
    char vet1[] = "arara";

    if (palindromo(vet1)){
        printf("%s eh palindromo",vet1);
    } else {
        printf("%s nao eh palindromo", vet1);
    }
}