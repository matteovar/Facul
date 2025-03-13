#include <stdio.h>

int findMax(int arr[], int n) {
  if (n == 1) {
    return arr[0]; 
  }

  int mid = n/2;

  int leftMax = findMax(arr, mid);
  int rightMax = findMax(arr+mid, n-mid);

  return fmax(leftMax, rightMax);
}

int main() {

  int arr[] = {2, 5, 8, 7, 3};
  int n = sizeof(arr)/sizeof(arr[0]);

  int max = findMax(arr, n);

  printf("O máximo é: %d", max);
  
  return 0;
}

//A complexidade continua sendo O(log n) 
