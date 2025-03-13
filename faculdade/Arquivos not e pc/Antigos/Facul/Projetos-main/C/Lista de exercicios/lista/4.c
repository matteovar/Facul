#include <stdio.h>

int countSubseqs(int arr[], int n) {
  int count = 1;
  
  for (int i = 1; i < n; i++) {
    if (arr[i] != arr[i-1]) {
      count++; 
    }
  }
  
  return count;
}

int main() {
  int arr1[] = {5, 2, 2, 3, 4, 4, 4, 4, 4, 1, 1};
  int n1 = sizeof(arr1) / sizeof(arr1[0]);
  
  printf("Subseqs in arr1: %d\n", countSubseqs(arr1, n1));

  int arr2[] = {3, 3, -1, -1, -1, 12, 12, 12, 3, 3};
  int n2 = sizeof(arr2) / sizeof(arr2[0]);

  printf("Subseqs in arr2: %d", countSubseqs(arr2, n2));

  return 0;
}

//A complexidade é O(n)