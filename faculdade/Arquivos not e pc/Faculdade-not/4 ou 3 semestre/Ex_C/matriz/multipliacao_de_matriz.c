#include<stdlib.h>
#include<stdio.h>
#include<time.h>

int main(){
    int matriz[2][3];
    int matriz2[3][2];
    int matriz3[2][2];

    srand(time(NULL));

    for (int i =0;i<2;i++){
        for (int j = 0;j<3;j++){
            matriz[i][j]= 1 + rand()%20;
        }
    }   

    for (int i =0;i<3;i++){
        for (int j = 0;j<2;j++){
            matriz2[i][j]= 1 + rand()%20;
        }
    }  

    for (int i =0; i<2; i++){
        for (int j = 0; j<2; j++){
            matriz3[i][j] = 0;
            for (int k = 0; k <3; k++){
                matriz3[i][j] += matriz[i][k] * matriz2[k][j];
            }
        }
    }

    printf("Matriz 1 \n");
    for (int i =0; i<2; i++){
        for (int j = 0; j<3; j++){
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    printf("Matriz 2\n");
    for (int i =0; i<3; i++){
        for (int j = 0; j<2; j++){
            printf("%d ", matriz2[i][j]);
        }
        printf("\n");
    }

    printf("Soma da matriz 1 e matriz 2: \n");
    for (int i =0;i<2;i++){
        for (int j = 0;j<2;j++){
            printf("%d ", matriz3[i][j]);
        }
        printf("\n");
    }
    return 0;
}

