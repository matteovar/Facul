#include <stdio.h>
#define N 8 // tamanho do tabuleiro

int tabuleiro[N][N]; 

bool permiteMovimento(int x, int y) {
  return (x >= 0 && x < N && y >= 0 && y < N && tabuleiro[x][y] == 0);
}

void marcaPosicao(int x, int y) {
  tabuleiro[x][y] = 1; 
}

void desmarcaPosicao(int x, int y) {
  tabuleiro[x][y] = 0;
}

bool percursoCavalo(int x, int y, int movimentos) {
  
  if(movimentos == N*N) 
    return true;
  
  // tenta todos os movimentos possíveis
  int dx[] = {2, 1, -1, -2, -2, -1, 1, 2}; 
  int dy[] = {1, 2, 2, 1, -1, -2, -2, -1};

  for(int i = 0; i < 8; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    
    if(permiteMovimento(nx, ny)) {
      marcaPosicao(nx, ny);
      
      if(percursoCavalo(nx, ny, movimentos+1))
        return true;
        
      desmarcaPosicao(nx, ny);
    }
  }
  
  return false;
}

int main() {

  int x0 = 0, y0 = 0; //posição inicial
  
  if(percursoCavalo(x0, y0, 1)) 
    printf("Percurso possível!\n");
  else
    printf("Percurso impossível!\n"