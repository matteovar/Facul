       
def buscaBinaria(vet,x):
    cont=0
    left=0
    right=(len(vet))-1
    if x>vet[right]: #limite do right
        return -1
    if x<vet[left]: #limite do left
        return -1
    while left<=right:
        cont += 1
        mid=(left+right)//2
        if vet[mid]==x:
            print("passos:",cont)
            return mid
        else:
            if vet[mid]<x:
                left=mid+1
            else:
                right=mid-1
    print("passos:",cont)
    return -1
        

vet=[61, 174, 197, 217, 309, 448, 503, 557, 629, 701, 831]

print(vet)
print(buscaBinaria(vet,60))
print(buscaBinaria(vet,503))

