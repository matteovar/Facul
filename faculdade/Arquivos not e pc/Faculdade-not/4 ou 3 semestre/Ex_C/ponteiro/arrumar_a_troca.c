
void troca (int *x, int *y) {
    int *temp;
    *temp = *x;
    *x = *y;
    *y = *temp;  //O erro esta no *temp pois esta colocando o endereco de memoria do x e do yn no endereco de memoria do temp
//Corrigindo

void troca(int *x, int *y){
    int *temp;
    temp = *x;
    *x*=y
    *y=temp
}

