import random

def criaA(n,m):
    matrizA=[]
    for i in range(n):
        listaA=[]
        for j in range(m):
            listaA.append(random.randint(1,50))
        matrizA.append(listaA)
    return matrizA

def criaB(n,m):
    matrizB=[]
    for i in range(n):
        listaB=[]
        for j in range(m):
            listaB.append(random.randint(1,50))
        matrizB.append(listaB)
    return matrizB

def imprime(matrizA):
    print("\n")
    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            print(matrizA[i][j],end=" ")
        print("\n")
    return matrizA

def imprimeB(matrizB):
    print("\n")
    for i in range(len(matrizB)):
        for j in range(len(matrizB[0])):
            print(matrizB[i][j],end=" ")
        print("\n")
    return matrizB

def soma(matrizA,matrizB):
    C=[]
    for i in range(len(matrizA)):
        tamsoma=[]
        for j in range(len(matrizA[0])):
            tamsoma.append(matrizA[i][j]+matrizB[i][j])
        C.append(tamsoma)
    return C          

def main():
    n=int(input("Digite as linhas:"))
    m=int(input("Digite as colunas:"))
    matrizA=criaA(n,m) 
    matrizB=criaB(n,m)
    imprime(matrizA)
    imprimeB(matrizB)
    print(soma(matrizA,matrizB))

main()
