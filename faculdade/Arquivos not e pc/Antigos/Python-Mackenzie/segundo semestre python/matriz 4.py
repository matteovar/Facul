import random
matriz=[]
n=3

def cria(n):
    for i in range(n):
        linha=[]
        for j in range(n):
            linha.append(random.randint(1,10))
        matriz.append(linha)
    return matriz

def diagonalSecundaria(matriz):
    aux=n-1
    soma=0
    for i in range(n):
        soma+=matriz[i][aux]
        aux-=1
    return soma

def imprime(matriz):
    for i in range(n):
        for j in range(n):
            print(matriz[i][j],end=" ")
        print("\n")
        
def main():
    cria(n)
    imprime(matriz)
    print("Soma da diagonal Secundaria:",diagonalSecundaria(matriz))

main()
