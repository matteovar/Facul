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

print(diagnonal(matriz))
