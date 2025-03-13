#include <math.h>
#include <stdbool.h>
#include <stdio.h>

int numeroPrimos(int n) {
  int j, cont = 1;

  for (j = 2; j <= n / 2; j++) {

    if (n % j == 0) {
      cont = 0;
    }
  }

  return cont;
}
int main() {
  int num1, num2, i, cont = 0;
  printf("Escreva dois numeros inteiros : ");
  scanf("%d%d", &num1, &num2);
  printf("Os numeros entre %d e %d sao: ", num1, num2);
  for (i = num1 + 1; i < num2; ++i) {
    cont = numeroPrimos(i);

    if (cont == 1) {
      printf("%d ", i);
    }
  }
  printf("\n");
  return true;
}
