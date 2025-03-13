#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int compare(char s1[], char s2[]){
    int i =0,j=0;
    while(s1[i] && s2[j]){
        if (s1[i]< s2[j])
            return -1;
        else if (s1[i]>s2[j])
            return 1;
        else {i++;j++;}
    }
    if (s1[i] == '\0' && s2[j]=='\0') return 0;
    else if (s1[i]=='\0') return -1;
    else return 1;

}
int main(void){
    printf("%d", compare("abacaxi","abacate"));
    printf("\n%d", strcmp("abacaxi","abacate"));
    return 0;
}
