#include <stdio.h>

void merge(int A[], int m, int B[], int n, int C[]) {
  
  int i = 0, j = 0, k = 0;
  
  while (i < m && j < n) {
    if (A[i] < B[j]) {
      C[k++] = A[i++];
    } else {
      C[k++] = B[j++]; 
    }
  }
  
  while (i < m) {
    C[k++] = A[i++];
  }
  
  while (j < n) {
    C[k++] = B[j++];
  }
}

int main() {

  int A[] = {1, 3, 5, 7};
  int B[] = {2, 4, 6};
  
  int C[7]; 
  
  merge(A, 4, B, 3, C);
  
  for (int i = 0; i < 7; i++) {
    printf("%d ", C[i]);
  }
  
  return 0;
}

//A complexidade é O(m+n)