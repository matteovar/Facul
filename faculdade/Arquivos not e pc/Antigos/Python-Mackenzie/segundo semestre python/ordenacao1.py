from todosjuntos import SelectionSort, BubbleSort, InsertionSort, MergeSort,QuickSort

def main():
    print("-------------BubbleSort----------")
    lista=[3,4,5,10,5,7]
    print("Lista original:",lista)
    BubbleSort(lista)
    print("BubbleSort:",lista)
main()

def main2():
    print("-------------SelectionSort------------")
    lista=[10,20,15,7,1,90]
    print("Lista Original:",lista)
    SelectionSort(lista)
    print("Lista Selection:",lista)
    
main2()

def main3():
    print("-------InsertionSort------------------")
    lista=[10,20,15,7,1,90]
    print("Lista original:",lista)
    InsertionSort(lista)
    print("InsertionSort:",lista)
main3()

def main4():
    print("---------MergeSort----------------")
    lista=[10,20,15,7,1,90]
    print("Lista original:",lista)
    MergeSort(lista,0,len(lista))
    print("Mergesort:",lista)
main4()

def main5():
    print("----------QuickSort-----------")
    lista=[10,20,15,7,1,90]
    print("Lista Original:", lista)
    QuickSort(lista,0,len(lista)-1)
    print("QuickSort:",lista)
main5()
