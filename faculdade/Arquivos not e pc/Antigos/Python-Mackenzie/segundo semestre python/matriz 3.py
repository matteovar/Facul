import random

matriz=[]
n=3

for i in range(n):
    linha=[]
    for j in range(n):
        if i==j:
            linha.append(random.randint(1,15))
        else:
            linha.append(0)
    matriz.append(linha)

for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print("\n")

    
def diagnonal(matriz):
    for l in range(len(matriz)):
        for h in range(len(matriz[0])):
            if l!=h and matriz[l][h]!=0:
                return False
    return True

def somadiagonal(matriz):
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
                soma+=matriz[i][j]
    return soma

print(diagnonal(matriz))
print(somadiagonal(matriz))
