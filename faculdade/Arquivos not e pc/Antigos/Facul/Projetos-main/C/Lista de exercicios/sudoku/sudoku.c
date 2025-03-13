#include <stdio.h>

void mostra_matriz(int m[4][4]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      printf("%d ", m[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

int valor_valido(int valor, int m[4][4], int linha, int coluna) {
  for (int i = 0; i < 4; i++) {
    if (m[linha][i] == valor || m[i][coluna] == valor)
      return 0;
  }
  return 1;
}

void sudoku(int m[4][4], int linha, int coluna) {
  if (coluna == 4) {
    linha = linha + 1;
    coluna = 0;
  }
  if (linha == 4) {
    mostra_matriz(m);
  } else if (m[linha][coluna] > 0) {
    sudoku(m, linha, coluna + 1);
  } else {
    for (int i = 1; i <= 4; i++) {
      if (valor_valido(i, m, linha, coluna)) {
        m[linha][coluna] = i;
        sudoku(m, linha, coluna + 1);
        m[linha][coluna] = 0;
      }
    }
  }
}

int main() {
  int matriz[4][4] = {{0, 2, 4, 0}, {1, 0, 0, 3}, {4, 0, 0, 2}, {0, 1, 3, 0}};

  printf("Matriz Inicial:\n");
  mostra_matriz(matriz);
  
  printf("Matriz Final:\n");
  sudoku(matriz, 0, 0);


  return 0;
}
