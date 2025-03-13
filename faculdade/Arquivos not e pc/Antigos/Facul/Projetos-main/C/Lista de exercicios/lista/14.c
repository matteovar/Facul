#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int A[MAX];
int n;
int melhorSoma = 0;

void calculaSoma(int perm[], int k) {
  if (k == n) {
    int soma = 0;
    for (int i = 0; i < n-1; i++) {
      soma += abs(perm[i] - perm[i+1]);
    }
    if (soma > melhorSoma) {
      melhorSoma = soma; 
    }
    return;
  }

  for (int i = 0; i < n; i++) {
    if (usado[i] == 0) {
      perm[k] = A[i];
      usado[i] = 1;
      calculaSoma(perm, k+1);
      usado[i] = 0; 
    }
  }
}

int somaElegante() {
  int perm[n];
  int usado[n];
  for (int i = 0; i < n; i++) {
    usado[i] = 0;
  }

  calculaSoma(perm, 0);
  return melhorSoma; 
}