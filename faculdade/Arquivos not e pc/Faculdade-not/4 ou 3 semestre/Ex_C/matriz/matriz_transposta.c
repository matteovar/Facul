#include<stdlib.h>
#include<stdio.h>
#include<time.h>

int main(){
    int taml = 3,tamc=3 ;
    int matriz[taml][tamc];
    int trans[tamc][taml];

    srand(time(NULL));

    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            matriz[i][j]= 1 + rand()%20;
        }
    }  

    for (int i = 0;i<tamc;i++){
        for(int j = 0;j<taml;j++){
            trans[j][i]= matriz[i][j];
        }
    }
    
    printf("Matriz Original\n");
    for (int i =0;i<taml;i++){
        for (int j = 0;j<tamc;j++){
            printf("%3d", matriz[i][j]);
        }
        printf("\n");
    }

    printf("Matriz Transposta \n");
    for (int i = 0;i<tamc;i++){
        for(int j = 0;j<taml;j++){
            printf("%3d", trans[i][j]);
        }
        printf("\n");
    }

    return 0;
}
