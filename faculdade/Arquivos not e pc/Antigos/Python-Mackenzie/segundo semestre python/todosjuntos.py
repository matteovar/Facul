def BubbleSort(lista):
    comparacoes=0
    trocas=0
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux

    return lista

def SelectionSort(lista):
    for i in range(len(lista)):
        min=i
        for j in range(i+1, len(lista)):
            if lista[min]>lista[j]:
                min=j
        aux=lista[i]
        lista[i]=lista[min]
        lista[min]=aux
    return lista

def InsertionSort(lista):
    for i in range(1,len(lista)):
        x=lista[i]
        j=i-1
        while j>=0 and x<lista[j]:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=x
    return  lista

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

def QuickSort(lista,inicio,fim):
    if inicio<fim:
        pivo =partition(lista,inicio,fim)
        QuickSort(lista,inicio,pivo-1)
        QuickSort(lista,pivo+1,fim)
        
def partition(lista,inicio,fim):
    pivo = lista[fim]
    i=inicio
    for j in range(inicio,fim):
        if lista[j]<=pivo:
            lista[j], lista[i]=lista[i],lista[j]
            i+=1
    lista[i],lista[fim]= lista[fim],lista[i]
    return i
