import random
n=int(input('valor'))
def geraVetor(vet):
    for i in range(len(vet)):
        vet[i]= random.randint(1,20)
    return vet

def ordem(vet):
    for i in range(len(vetor)-1):
        if vet[i]>vet[i+1]:
            return False
    return True

vet= [0]*n

vetor=geraVetor(vet)
vetor.sort()
print(vetor)
print(ordem(vetor))

