import random

def vetorA(vetor1):
    for i in range(len(vetor1)):
        vetor1[i]=random.randint(1,10)
    return(vetor1)

def vetorB(vetor2):
    for i in range(len(vetor2)):
        vetor2[i]=random.randint(1,10)
    return(vetor2)

def contador(vetor1,vetor2):
    cont=0
    for i in range(len(vetor1)):
        flag = False
        for j in range(len(vetor2)):
            if i !=j:
                if vetor1[i]==vetor2[j]:
                    flag=True
        if flag==False:
            cont+=1
    return cont



vetor1=[0]*5
vetor2=[0]*5

vetor1=vetorA(vetor1)
vetor2=vetorB(vetor2)


print(vetor2)

print(contador(vetor1,vetor2))
