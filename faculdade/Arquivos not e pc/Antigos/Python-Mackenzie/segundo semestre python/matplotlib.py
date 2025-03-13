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
            flag=False
        for j in range(len(lista)-1-i):
            if lista[j]>lista[j+1]:
                troca(lista,j,i+1)
                flag = True
            yield lista

def insertsortion(lista):
    for i in range(1,len(lista)):
        j=i
        while j>0 and lista[j]>lista[j-1]:
            troca(lista,i,j-1)
            j=-1
            yield lista

def selectionsort(A):
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

def main():
    N=int(input("Digite o numero de inteiros no grafico:"))
    method_msg = "Qual metodo desejado?\n(b)ubble\n(i)nsertion\n(s)election\n"
    method = input(method_msg)
    lista=[x+1 for x in range(N)]
    if method=="b" or "B":
        title="Bubble Sort"
        generator=bubblesort(lista)
    elif method=="i"or "I":
        title="Insertion Sort"
        generator=insertionsort(lista)
    else:
        title="Selection Sort"
        generator=selectionsort(lista)
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
    
    
main()

        
