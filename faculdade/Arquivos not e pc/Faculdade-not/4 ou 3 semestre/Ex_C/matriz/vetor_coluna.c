#include<stdlib.h>
#include<stdio.h>

int main(){
    int *v = (int *)calloc(4, sizeof(int));
    v[0] = 10;
    v[1] = 20;
    v[2] = 30;
    v[3] = 40;
     for(int i =0;i<4;i++){
        printf("%d \n",v[i]);
        printf("%d \n",(v[i]+1));
    }
}

int *v = (int *)calloc(4, sizeof(int)); 
v[0] = 10; 
v[1] = 20; 
v[2] = 30; 
v[3] = 40;
printf("%d",*v); 
printf("%d",*(v+1));
