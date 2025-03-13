import random

matriz=[]
n=10

def criamatriz(n):
    for i in range(n):
        linha=[]
        for j in range(n):
            linha.append(random.randint(1,25))
        matriz.append(linha)
    return matriz

def imprime(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=" ")
        print("\n")


def somadiagonal(matriz):
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
                soma+=matriz[i][j]
    return soma

def somadiagonalsec(matriz):
    aux=n-1
    soma=0
    for i in range(n):
        soma+=matriz[i][aux]
        aux-=1
    return soma
def acimadiagonal(matriz):
    soma_col=0
    soma_lin=0
    for i in range(n):
        soma_col+=matriz[n-1][i]
        soma_lin+=matriz[i][i]
    soma_acima=0
    soma=0
    for i in range(n):
        for j in range(n):
            if j>1:
                soma_acima+=matriz[i][j]
            soma+=matriz[i][j]
    return soma
        

        

def main():
    criamatriz(n)
    imprime(matriz)
    print("Diagonal Principal:",somadiagonal(matriz))
    print("Diagonal Secundaria:",somadiagonalsec(matriz))
    print("Diagonal Acima:",acimadiagonal(matriz))
    print("Diagonal Abaixo:",abaixodiagonal(matriz))
    

main()
            
