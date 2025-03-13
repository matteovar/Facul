#include <stdio.h>

#define N 5 // tamanho do vetor

void ordenaVetor(int vetor[], int n) {
  if (n == 1) return; // caso base
  
  for (int i = 0; i < n - 1; i++) {
    if (vetor[i] > vetor[i+1]) {
      // troca os elementos
      int temp = vetor[i];
      vetor[i] = vetor[i+1]; 
      vetor[i+1] = temp;
    }
  }
  
  ordenaVetor(vetor, n - 1); //chamada recursiva
}

int main() {
  int vetor[N] = {5, 3, 2, 4, 1};
  
  ordenaVetor(vetor, N);
  
  for (int i = 0; i < N; i++) {
    printf("%d ", vetor[i]); 
  }

  return 0;
}