import random
import time


def vetor(matriz):
    tempo=time.time()
    comparacoes=0
    trocas=0
    for i in range(10000):
        comparacoes+=1
        trocas+=1
        matriz.append(random.randint(1,100))
    tempo2=time.time()-tempo
    return matriz,tempo2,trocas,comparacoes


def main3():
    matriz=[]
    vetor(matriz)
    matriz,tempo2,trocas,comparacoes=vetor(matriz)
    print(matriz)
    print("comp:",comparacoes)
    print("trocas:",trocas)
    print("tempo:",tempo2)
main3()
