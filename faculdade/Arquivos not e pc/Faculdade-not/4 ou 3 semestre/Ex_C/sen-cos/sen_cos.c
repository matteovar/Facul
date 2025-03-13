#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define PI 3.14
struct coseno_sen{
    double sen;
    double con;
};

int sencon(double graus, struct coseno_sen* transforma){
    double radianos = graus * PI/180.0;

    (*transforma).con = cos(radianos);
    (*transforma).sen = sin(radianos);
}

int main(void){
    double   graus = 60.0;
    struct coseno_sen sen__con;

    sencon(graus,&sen__con);
    printf("O sen do grau %.2f 'e  de %.2f", graus,sen__con.sen);
    printf("\nO cos do grau %.2f 'e de %.2f", graus,sen__con.con);

    return 0;
}