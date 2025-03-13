#include <stdio.h>
#include <stdlib.h>

int main(void){

    int i ;

    for (i = 10; i<=20; i++){
            if (i % 2 == 0){
                printf("%d 'e par\n", i);
            }else{
                printf("%d 'e impar\n", i);
            }
    }
    return 0;
}
