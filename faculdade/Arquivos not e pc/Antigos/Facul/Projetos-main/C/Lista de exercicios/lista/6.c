#include <stdio.h>

int main() {
  int arr[] = {7, 9, 5, 4, 5, 4, 8, 6};
  int n = sizeof(arr) / sizeof(arr[0]);
  
  for (int i = 0; i < n-1; i++) {
    for (int m = 1; m <= (n-i)/2; m++) {
      int equal = 1;
      for (int j = 0; j < m; j++) {
        if (arr[i+j] != arr[i+m+j]) {
          equal = 0;
          break;
        }
      }
      if (equal) {
        printf("i = %d, m = %d\n", i, m);
        return 0;
      }
    }
  }
  
  printf("Não existem segmentos iguais\n");

  return 0;
}

//A complexidade é O(n^2)