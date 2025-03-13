import random

def criaMatriz(M,N):
    matriz=[]
    for i in range(M):
        tamanho=[]
        for j in range(N):
            tamanho.append(random.randint(1,100))
        matriz.append(tamanho)
    return matriz

def imprime(matriz):
    print("\n")
    print("Matriz original:")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=" ")
        print("\n")
    return matriz

def matrizTransposta(matriz):
    print("\n")
    print("Matriz Transposta:")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[j][i], end=" ")
        print("\n")
    return matriz

def main():
    M=int(input("Digite a linha:"))
    N =int(input("Digite a coluna:"))
    matriz=criaMatriz(M,N)
    imprime(matriz)
    matrizTransposta(matriz)

main()
