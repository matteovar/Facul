//int x = 50;

int main(){
    int a =10, b =20;

    int *p, *q;

    p=&a;

    q = &b;

    printf("a = %d e b = %d", a,b);

    troca(p,q);
    troca(p,q);

    printf("\na = %d e b = %d",a,b);

}

void troca(int *x, int *y){
    int temp;
    temp = *x;
    *x=*y;
    *y=temp;

}
/*
    int x  = 10;

    int *p = &x;

    int **r = &p;

    printf("%d\n",**r);

    **r = 100;

    printf("%d", x);
}
*/

/*
    int *p,*q;
    int a , b;

    a =10;
    b = 20;

    p = &a;

    q = &b;

    p = q;

    printf("a = %d e b = %d", a ,b );

*/

/*
    int  a = 5, b ;

    int *p;

    p = &a;

    b = *p +10;

    printf("%d  %d  %d  %p", a,b,*p,p);
*/
/*
    f(a,b);

    printf("%d %d ", a,b);

    troca(a,b);

    printf("%d %d ", a, b);

    printf("%d",x);

void f(int a , int b){
    a=10;
    b=20;
    x=50;
}

//funcao inutil FDP

void troca(int a, int b){
    int temp;
    temp = a;
    a= b;
    b=temp;
}
*/
