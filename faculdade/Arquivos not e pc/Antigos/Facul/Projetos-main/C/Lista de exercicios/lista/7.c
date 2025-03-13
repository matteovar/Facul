#include <stdio.h>

int maxSumSubseq(int arr[], int n) {
  
  int maxSum = 0;
  int currSum = 0;
  
  for (int i = 0; i < n; i++) {
    currSum += arr[i];
    if (currSum < 0) {
      currSum = 0; 
    }
    maxSum = fmax(maxSum, currSum);
  }
  
  return maxSum;
}

int main() {

  int seq[] = {5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1};
  
  printf("Max sum: %d\n", maxSumSubseq(seq, 12));
  
  return 0;
}

//A complexidade é O(n),
