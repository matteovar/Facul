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

#lista=[1,2,3,4,5]
lista=[13,3,4,5,7,10,20]
##lista=[10,9,8,7,6,5,4,3,2,1]
print(lista)
QuickSort(lista,0,len(lista)-1)
print(lista)
