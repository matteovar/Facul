import random

def recebe(vetor):
    for i in range(len(vetor)):
        vetor[i]=random.randint(1,10)
    return vetor

def recebe2(vetor2):
    for i in range(len(vetor2)):
         vetor2[i]=int(input("Digite um numero:"))
    return vetor2

def iguais(vetor,vetor2):                
    while True:
        try:
            for i in range(len(vetor)):
                flag = False
                for j in range(len(vetor2)):
                    if i==j:
                        if vetor[i]==vetor[j]:
                            flag=True
                            print("Posicao do vetor:",vetor.index(vetor2[j]))
            break
        except ValueError:
            print("Posicao nao encontrada porem valor do vetor -1:",vetor2[i]-1)
            break
            

        
    


vetor=[0]*5
vetor2=[0]*1
print(recebe(vetor))
recebe2(vetor2)
iguais(vetor,vetor2)


