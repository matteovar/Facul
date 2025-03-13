import random

def criarvetor(vetor1):
    for i in range(len(vetor1)):
        vetor1[i]=random.randint(1,10)
    return vetor1

def criarvetor2(vetor2):
    for i in range(len(vetor2)):
        vetor2[i]=random.randint(1,10)
    return vetor2

def ordena(vetor1,vetor2):
    vetor3=[0]*(len(vetor1)+len(vetor2))
    k=0
    y=0
    for i in range(len(vetor3)):
        if k>=len(vetor1):
            vetor3[i]=vetor1[i]
            y+=1
        elif y>=len(vetor2):
            vetor3[i]=vetor1[i]
            k+=1
        elif vetor1<=vetor2:
            vetor3[i]=vetor1[i]
            k+=1
        else:
            vetor3[i]=vetor2[i]
            y+=1
    return vetor3



def main():
    m=int(input("Digite o tamanho do vetor:"))
    n=int(input("Digite o tamanho do outro vetor:"))
    vetor1=[0]*m
    vetor2=[0]*n
    vetor1=criarvetor(vetor1)
    vetor2=criarvetor2(vetor2)
    print(vetor1)
    print(vetor2)
    vetor3=ordena(vetor1,vetor2)
    print(vetor3)

main()
