import random

vetor=[0]*10

def geraVetor(vetor):
    for i in range(len(vetor)):
        vetor[i]=random.randint(1,100)
    return vetor

def imprimi(vetor):
    for i in range(len(vetor)):
        print(vetor[i],end =" ")

def calculamedia(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma+=vetor[i]  
    return soma/len(vetor)

def inverter(vet1,vet2):
    for i in range(len(vet1)): #coloca o tamanho do vetor Vet1  
        vet2[i]=vet1[len(vetor)-1-i] #fala que o vet2 vai pegar a distancia do vet1 
    return vet2

def inverter2(vet1):
    for i in range(len(vetor)):
        vet1[i]=vetor[len(vetor)-1-i]
    return vet1
"""
n = len(vet1)-1
    for i in range(len(vet1)//2):
        aux =  vet1[i]
        vet1[i]=vet1[n-i]
        vet1[n-i]=aux
    
    return vet1
"""
    
   

vetor=[0]*10
vet2= [0]*10
vet1= [0]*10

geraVetor(vetor)
imprimi(vetor)
print(f'\nMedia: {calculamedia(vetor)}')
print(inverter(vetor,vet2))
print(inverter2(vet1))
