#include <stdio.h>

int maxIncreasingSubseq(int arr[], int n) {
  int maxLen = 1;
  int currLen = 1;
  
  for (int i = 1; i < n; i++) {
    if (arr[i] > arr[i-1]) {
      currLen++;
      maxLen = fmax(maxLen, currLen);
    } else {
      currLen = 1; 
    }
  }
  
  return maxLen;
}

int main() {
  int seq1[] = {5, 10, 3, 2, 4, 7, 9, 8, 5};
  int seq2[] = {10, 8, 7, 5, 2};
  
  printf("Max length seq1: %d\n", maxIncreasingSubseq(seq1, 9));
  printf("Max length seq2: %d\n", maxIncreasingSubseq(seq2, 5));
  
  return 0;
}

//A complexidade é O(n)