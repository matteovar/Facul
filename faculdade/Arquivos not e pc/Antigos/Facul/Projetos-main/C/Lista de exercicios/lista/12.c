#include <stdbool.h>

bool podeFazerQuadrado(int palitos_de_fosforos[], int n) {

  int soma = 0;
  for(int i = 0; i < n; i++) {
    soma += palitos_de_fosforos[i]; 
  }
  
  if(soma % 4 != 0) {
    return false; 
  }

  return subsetsSum(palitos_de_fosforos, n, soma/4); 
}

bool subsetsSum(int arr[], int n, int sum) {
  
  if (sum == 0)
    return true;

  if (n == 0 && sum != 0)
    return false;

  if (arr[n-1] > sum)
    return subsetsSum(arr, n-1, sum);

  return subsetsSum(arr, n-1, sum) || 
         subsetsSum(arr, n-1, sum-arr[n-1]);
}