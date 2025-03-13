import random
matriz=[]
n=100

def vetor(matriz):
    for i in range(n):
        matriz.append(random.randint(1,100))
        
    return matriz

def BubbleSort(matriz):
    for k in range(len(matriz)):
        cont=0
        for j in range(len(matriz)-1-k):
            if vetor[i]>v[i+1]:
                temp=vetor[i]
                v[i]=v[i+1]
                v[i+1]=temp
                cont+=1
    return matriz,cont

def main():
    matriz=[]
    n=100
    vetor(vetor)
    BubbleSort(vetor)
main()
                
