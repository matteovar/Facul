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
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=" ")
        print("\n")

        
def Maior(matriz):
    maior=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]>maior:
                maior=matriz[i][j]
    return maior


def main():
    M=int(input("Digite a linha:"))
    N =int(input("Digite a coluna:"))
    matriz=criaMatriz(M,N)
    imprime(matriz)
    print("Maior 'e:",Maior(matriz))

main()
