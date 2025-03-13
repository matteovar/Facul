#include <stdio.h>
#include <stdlib.h>


int main(void){
    int matriz[4][2];

    for (int i = 0; i<4;i++){
        for (int j =0; j<2;j++){
            scanf("%d", &matriz[i][j]);
        }
    }
    for (int i = 0;i<4;i++){
        for (int j = 0;j<2;j++){
            printf("%d-%d[%d] ",i,j, matriz [i][j]);
        }
        printf("\n");
    }
}
