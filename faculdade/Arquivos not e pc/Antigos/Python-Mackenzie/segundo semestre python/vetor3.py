import random

def vetorA(vetor1):
    for i in range(len(vetor1)):
        vetor1[i]=random.randint(1,10)
    return(vetor1)

def vetorB(vetor2):
    for i in range(len(vetor2)):
        vetor2[i]=random.randint(1,10)
    return(vetor2)

def intersecao(vetor1,vetor2):
    string = ""
    for i in range(len(vetor1)):
        for x in range(len(vetor2)):
            if vetor1[i]==vetor2[x]:
                string += str(vetor1[i]) + " "
    return string



vetor1=[0]*5
vetor2=[0]*3

vetor1=vetorA(vetor1)
vetor2=vetorB(vetor2)

print(vetor1)
print(vetor2)

print(intersecao(vetor1,vetor2))
