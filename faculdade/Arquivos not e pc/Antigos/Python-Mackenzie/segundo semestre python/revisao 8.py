def buscasequencial(matriz,chave):
    for i in range(len(matriz)):
        if matriz[i]==chave:
            return i
    return -1
def binaria(matriz,chave):
    inicio=0
    cont=0
    fim=len(matriz)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if matriz[meio]==chave:
            return meio
        elif matriz[meio]>chave:
            fim=meio-1
        else:
            inicio=meio+1
        cont+=1
    return -1
    

def main():
    matriz=[20,5,15,24,67,45,1,76]
    print(buscasequencial(matriz,24))
    print(binaria(matriz,24))
    
main()
