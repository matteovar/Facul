import random
import time


def vetor(matriz):
    for i in range(10):
        matriz.append(random.randint(1,100))
    return matriz


def BubbleSort(matriz):
    cont=0
    seconds=time.time()
    comparacoes=0
    for i in range(len(matriz)):
        for j in range(len(matriz)-1-i):
            comparacoes+=1
            if matriz[j]>matriz[j+1]:
                temp=matriz[j]
                matriz[j]=matriz[j+1]
                matriz[j+1]=temp
                cont+=1
    tempofinal=time.time()-seconds
    return matriz,cont,comparacoes,tempofinal

def SelectionSort(matriz):
    cont2=0
    tempo2=time.time()
    comp2=0
    for i in range(len(matriz)):
        min=i
        for j in range(i+1, len(matriz)):
            comp2+=1
            if matriz[min]>matriz[j]:
                min=j
                cont2+=1
        aux=matriz[i]
        matriz[i]=matriz[min]
        matriz[min]=aux
    timefinal2=time.time()-tempo2
    return cont2,timefinal2,comp2,matriz

def InsertionSort(lista):
    cont2=0
    tempo2=time.time()
    comp2=0
    for i in range(1,len(matriz)):
        x=matriz[i]
        j=i-1
        comp2+=1
        while j>=0 and x<matriz[j]:
            matriz[j+1]=matriz[j]
            j-=1
            cont2+=1
        matriz[j+1]=x
    tempo2=time.time()-tempo2
    return  cont2,tempo2,comp2,matriz

def main():
    matriz=[]
    vetor(matriz)
    print("---------Bubble----------------")
    print("--------------Origianal-------------------")
    print(matriz)
    matriz,cont,comparacoes,tempofinal=BubbleSort(matriz)
    print("---------------Ordenado---------------------")
    print(matriz)
    print("trocas:",comparacoes)
    print("tempo:",tempofinal)
    print("contador:",cont)
main()

def main2():
    matriz=[]
    vetor(matriz)
    print("----------------Selection-------------")
    print("--------------Origianal-------------------")
    print(matriz)
    cont2,timefinal2,comp2,matriz=SelectionSort(matriz)
    print("---------------Ordenado---------------------")
    print(matriz)
    print("trocas",comp2)
    print("tempo:",timefinal2)
    print("Contador:",cont2)
main2()

def main3():
    matriz=[]
    vetor(matriz)
    print("----------------Insert-------------")
    print("--------------Origianal-------------------")
    print(matriz)
    cont2,tempo2,comp2,matriz=InsertionSort(matriz)
    print("---------------Ordenado---------------------")
    print(matriz)
    print("trocas",comp2)
    print("tempo:",tempo2)
    print("Contador:",cont2)
main3()
    
