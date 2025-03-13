import random
def geraVetor(vetor):
    for i in range(len(vetor)):
        vetor[i]=random.randint(1,100)
    return vetor

def inverter(vet1,vet2):
    for i in range(len(vet1)):
        vet2[i]=vet1[len(vetor)-1-i]
    return vet2

def inverter2(vet1):
    for i in range(len(vetor)):
        vet1[i]=vetor[len(vetor)-1-i]
        
    
    return vet1

vetor=[0]*10
vet2= [0]*10
vet1= [0]*10

print(f'vetor original: {geraVetor(vetor)}')
print(f'Invertido com auxilio: {inverter(vetor,vet2)}')
print(f'Invertido sem auxilio: {inverter2(vet1)}')
