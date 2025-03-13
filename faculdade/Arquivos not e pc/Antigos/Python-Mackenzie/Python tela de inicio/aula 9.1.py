notas = []
def msg():
    print("Digite suas notas: ")
    for i in range(5):
        n = float(input("Notas: "))
        while n<0 or n>10:
            n = float(input("Notas: "))
        notas.append(n)

    print(notas)

def media():
    return sum(notas)/len(notas)

def acha_menor():
    return min(notas)

def acha_maior():
    return max(notas)

def lugar_maior(maior):
    i = notas.index(maior)
    return i+1
    
def lugar_menor(menor):
    i = notas.index(menor)
    return i+1

def nota_10():
    for x in notas:
        if x ==10:
            print("Parabens, voce tirou 10 ")
    
def main():
    msg()
    print("media: ", media())
    maior = acha_maior()
    menor = acha_menor()
    print(" maior numero da lista: ",maior)
    print("menor numero da lista: ",menor)
    print("lugar do maior numero: ",lugar_maior(maior))
    print("lugar do menor numero: ",lugar_menor(menor))
    nota_10()
    print(notas)
    
    
    
main()
