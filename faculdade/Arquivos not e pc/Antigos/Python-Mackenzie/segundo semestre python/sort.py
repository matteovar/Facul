import random

def matriz(l,c):
    matriz = []
    for i in range(l):
        linha = [] 
        for j in range(c):        
            linha.append(random.randint(1,9))
        matriz.append(linha)
    return matriz


def abaixo_da_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if len(matriz)-1 == j + i:
                soma += matriz[i][j]
            else:
                if i + j > len(matriz)-1:
                    soma += matriz[i][j]
    return soma
    


def main():
    l=int(input("DIgite o tamanho de linha:"))
    c=int(input("Digite o numero de colunas:"))
    vetor= matriz(l,c)
    for i in range(len(vetor)):
        print(vetor[i])
    soma_abaixo = abaixo_da_diagonal(vetor)
    print('Soma abaixo da diagonal:', soma_abaixo)

main()
    
