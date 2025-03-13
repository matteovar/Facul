#include <stdio.h>
#include <stdlib.h>


void converte(int min, int *m, int *h){
    *h = min/60;

    *m = min % 60;

    if  (m>=59){
    *h += *m / 60;
        *m %= 60;
    }



}

int main(void){

    int minutos=125;
    int horas, resto;
    converte(minutos, &resto,&horas);

    printf("O valor convertido de %d min  para %d hrs e  %d min", minutos, horas,resto);
}
