#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
   int n = 10;
   int v[n];


   srand(time(NULL));

   for (int i=0;i<10;i++){
       v[i]=1+rand() %20;
   }
   printf("\n\n");
   for (int i = 0;i<10;i++){
      printf("%d \n", v[i]);
   }
   printf("\n\n");
}