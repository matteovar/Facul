carros= []
litros = []
def entrada_carro():
    for d in range(4):
        n = input()
        carros.append(n)

def entrada_consumo():
    for i in range(4):
        n1 = int(input())
        litros.append(n1)
        
def economico():
    menor = min(litros)
    h = litros.index(menor)
    return carros[h]

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())
    

main()
