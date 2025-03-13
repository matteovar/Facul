#append(acresecenta um arquivo no final da lista).
n=[]
print("Digitie 5 numero: ")

for i in range(5):
    x = int(input())
    n.append(x)
print(n)

#menor e maior numero da lista
print(min(n))
print(max(n))

#quantos elementos o numero tem na lista
print(n.count(10))

#index(mostra aonde t ao elemento)
print(n.index(10))
