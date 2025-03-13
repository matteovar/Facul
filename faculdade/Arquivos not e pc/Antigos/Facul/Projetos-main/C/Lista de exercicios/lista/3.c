#include <math.h>
#include <stdio.h>

double raizQ(double x, double x0, double epsilon) {
  double x1 = (x0 + x/x0) / 2;
  if (fabs(x1*x1 - x) <= epsilon) {
    return x1;
  }
  else {
    return raizQ(x, x1, epsilon); 
  }
}

int main() {
  double x = 13;
  double x0 = 3.2;
  double epsilon = 0.001;

  printf("Raiz quadrada de %lf = %lf\n", x, raizQ(x, x0, epsilon));
  
  return 0;
}

//A complexidade no pior caso é O(log(1/ε))