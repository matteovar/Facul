#include <stdbool.h>
#include <stdio.h>

int main() {
  int numero1, j = 1, i, cont = 0;

  printf("Insira um numero: ");
  scanf("%d", &numero1);

  int vet[numero1];

  for (i = 0; i < numero1; ++i) {

    vet[i] = j;
    if ((j % 2) == 0) {
      cont = cont + j;
    }
    j++;
  }

  printf("A soma dos numeros pares do vetor é: %d\n", numero1);

  return 0;
}