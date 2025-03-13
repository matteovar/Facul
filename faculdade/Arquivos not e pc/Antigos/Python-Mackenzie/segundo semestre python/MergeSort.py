def MergeSort(lista,inicio,fim):
    if (fim-inicio)>1:
        meio=(inicio+fim)//2
        MergeSort(lista,inicio,meio)
        MergeSort(lista,meio,fim)
        Merge(lista,inicio,meio,fim)

        
def Merge(lista,inicio,meio,fim):
    esquerda=lista[inicio:meio]
    direita=lista[meio:fim]
    top_e,top_d=0,0
    for k in range(inicio,fim):
        if top_e>=len(esquerda):
            lista[k]=direita[top_d]
            top_d+=1
        elif top_d>=len(direita):
            lista[k]=esquerda[top_e]
            top_e+=1
        elif esquerda[top_e]< direita[top_d]:
            lista[k]=esquerda[top_e]
            top_e+=1
        else:
            lista[k]=direita[top_d]
            top_d+=1
            

#lista=[1,2,3,4,5,6,7,8]
#lista=[15,3,26,45,9,8,4,8,12,45,9,78,23,101,45]
lista=[8,7,6,5,4,3,2,1]
print(lista)
MergeSort(lista,0,len(lista))
print(lista)
