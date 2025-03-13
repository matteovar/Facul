#include <stdio.h>

void printSequencias(int m, int n, char *sequencia, int i) {
  
  if (i == m+n) {
    printf("%s\n", sequencia);
    return;
  }
  
  if (m > 0) {
    sequencia[i] = 'A';
    printSequencias(m-1, n, sequencia, i+1);
  }
  
  if (n > 0) {
    sequencia[i] = 'B';
    printSequencias(m, n-1, sequencia, i+1); 
  }
}

int main() {
  int m = 3, n = 1;
  char sequencia[4];
  
  printSequencias(m, n, sequencia, 0);
  
  return 0;
}
