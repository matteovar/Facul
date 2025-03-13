#include <stdio.h>

#define MAX 100
int n, soma;
int P[MAX];

bool subsetSum(int i, int parcial) {
  if (parcial == soma) 
    return true;

  if (i == n || parcial > soma) 
    return false;

  return subsetSum(i+1, parcial + P[i]) || 
         subsetSum(i+1, parcial);
}

int main() {
  
  //entrada de dados
  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    scanf("%d", &P[i]); 
  }
  scanf("%d", &soma);

  if (subsetSum(0, 0)) {
    printf("Existe subconjunto com soma %d\n", soma);
  } else {
    printf("Nao existe subconjunto com soma %d\n", soma);
  }

  return 0;
}