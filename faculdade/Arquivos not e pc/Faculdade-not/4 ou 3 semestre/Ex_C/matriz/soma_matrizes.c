#include<stdlib.h>
#include<stdio.h>
#include<time.h>

int main(){
    int taml = 2, tamc=4;
    int matriz[taml][tamc];
    int matriz2[taml][tamc];
    int matriz3[taml][tamc];

    srand(time(NULL));

    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            matriz[i][j]= 1 + rand()%20;
        }
    }     

    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            matriz2[i][j]= 1 + rand()%20;
        }
    }     

    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            matriz3[i][j] = matriz[i][j] + matriz2[i][j];
        }
    }
    printf("Matriz 1 \n");
    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            printf("%3d", matriz[i][j]);
        }
        printf("\n");
    }
    
    printf("Matriz 2\n");
    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            printf("%3d", matriz2[i][j]);
        }
        printf("\n");
    }
    
    printf("Soma da matriz 1 e matriz 2: \n");
    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            printf("%2d ", matriz3[i][j]);
        }
        printf("\n");
    }
    return 0;
}
