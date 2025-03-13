#include <stdio.h>

void printBinary(int n, int num) {
  if (n == 0) { 
    printf("%d\n", num);
    return;
  }
  
  printBinary(n-1, num*10);
  printBinary(n-1, num*10 + 1);
}

int main() {
  int n = 3;
  printBinary(n, 0);
  
  return 0;  
}

//A complexidade é O(2^n) 