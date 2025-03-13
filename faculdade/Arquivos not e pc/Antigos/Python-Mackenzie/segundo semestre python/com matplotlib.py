import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def troca(lista,i,j):
    if i!=j:
        lista[i],lista[j]=lista[j],lista[i]

def bubblesort(lista):

    if len(lista)==1:
        return
    flag=True
    for i in range(len(lista)-1):
        if not flag:
            break
        flag=False
        for j in range(len(lista)-1-i):
            if lista[j]>lista[j+1]:
                troca(lista,j,j+1)
                flag = True
            yield lista

def insertsortion(lista):
    for i in range(1,len(lista)):
        j=i
        while j>0 and lista[j]<lista[j-1]:
            troca(lista,i,j-1)
            j-=1
            yield lista

def selectionsort(lista):
    if len(lista) == 1:
        return
    for i in range(len(lista)):
        min_val = lista[i]
        minimo = i
        for j in range(i, len(lista)):
            if lista[j] < min_val:
                min_val = lista[j]
                minimo = j
            yield lista
        troca(lista, i, minimo)
        yield lista
        
def quicksort(lista, start, end):
    if start >= end:
        return
    pivot = lista[end]
    pivotIdx = start

    for i in range(start, end):
        if lista[i] < pivot:
            swap(lista, i, pivotIdx)
            pivotIdx += 1
        yield lista
    swap(lista, end, pivotIdx)
    yield lista

    yield from quicksort(lista, start, pivotIdx - 1)
    yield from quicksort(lista, pivotIdx + 1, end)

def mergesort(lista, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(lista, start, mid)
    yield from mergesort(lista, mid + 1, end)
    yield from merge(lista, start, mid, end)
    yield lista

def merge(lista, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if lista[leftIdx] < lista[rightIdx]:
            merged.append(lista[leftIdx])
            leftIdx += 1
        else:
            merged.append(lista[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(lista[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(lista[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        lista[start + i] = sorted_val
        yield lista


if __name__=="__main__":
    N=int(input("Digite o numero de inteiros no grafico:"))
    method_msg = "Qual metodo desejado?\n(b)ubble\n(i)nsertion\n(s)election\n"
    method = input(method_msg)
    lista=[x+1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(lista)
    if method=="b":
        title="Bubble Sort"
        generator=bubblesort(lista)
    elif method=="i":
        title="Insertion Sort"
        generator=insertsortion(lista)
    elif method=="s":
        title="Selection Sort"
        generator=selectionsort(lista)
    elif method=="m":
        title = "Merge Sort"
        generator=mergesort(lista, 0, N-1)
    fig,ax=plt.subplots()
    ax.set_title(title)
    bar_rects=ax.bar(range(len(lista)),lista,align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    
    def update_fig(lista, rects, iteration):
        for rect, val in zip(rects, lista):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()


        
