import random


def escolha_numeros(vetor):
    for i in range(len(vetor)):
        vetor[i]=int(input("Digite os numeros inteiros: "))
    return vetor

def crescente(vetor):
   for i in range(len(vetor)):
       if vetor[i]<vetor[i+1]:
           return True
   return False
            


vetor=[0]*5

print(escolha_numeros(vetor))
print(crescente(vetor))


