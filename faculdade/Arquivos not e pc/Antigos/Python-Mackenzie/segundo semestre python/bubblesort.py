

def BubbleSort(L):
    comparacoes=0
    trocas=0
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            comparacoes+=1
            if L[j]>L[j+1]:
                trocas+=1
                aux=L[j]
                L[j]=L[j+1]
                L[j+1]=aux

    return L,comparacoes,trocas

def main():
    L=[5,6,8,10,3,2,1,15]
    L,comparacoes,trocas=BubbleSort(L)
    print(L)
    print("Trocas:",trocas)
    print("Comparacoes:", comparacoes)
main()
