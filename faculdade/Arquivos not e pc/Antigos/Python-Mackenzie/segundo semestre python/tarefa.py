def busca(vetor,x):
    cont=0
    for i in range(len(vetor)):
        cont+=1
        if vetor[i]==x:
            print("Passos:",cont)
            return i
    print("Passos:",cont)
    return-1

vetor=[-10,-5,-1,0,3,5,10,25,36,70]
print(busca(vetor,5))
print(busca(vetor,25))
