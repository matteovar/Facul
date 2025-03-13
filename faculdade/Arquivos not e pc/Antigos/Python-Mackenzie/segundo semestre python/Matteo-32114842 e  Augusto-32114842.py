'''
Entrega do Trabalho _- Algoritmos e Programação II
Nós,

Augusto Carrera - 32114842
Matteo Domiciano Varnier - 32158238

declaramos que
todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
'''
import random
entrada=open('entrada.txt','w', encoding="utf8")
saida=open('saida.txt','w', encoding="utf8")

def geravetor(vetor,d):
    for i in range(d):
        vetor.append(random.randint(0,100))
    return vetor

def decisao(jogador1,jogador2,ordem):
    print("Será jogado par ou impar para ver quem começará o jogo")
    print("")
    print("Para que seja justo, o programa decidira aleatoriamente quem representa os numeros pares e quem representa os numeros impares")
    print("")
    print(jogador1,"digite um numero para o par ou impar")
    dec1=int(input())
    print(jogador2,"digite um numero para o par ou impar")
    dec2=int(input())
    soma = dec1+dec2
    dec3=random.randint(1,2)
    if dec3 == 1:
        if soma%2 == 0:
            print(jogador1," representava os numeros pares, portanto, começará")
            ordem = 1
        else:
            print(jogador2," representava os numeros impares, portanto, começará")
            ordem = 2
    if dec3 == 2:
        if soma%2 == 0:
            print(jogador2," representava os numeros pares, portanto, começará")
            ordem = 2
        else:
            print(jogador1," representava os numeros impares, portanto, começará")
            ordem = 1
    return ordem

def bubble_sort(h):
    for i in range(len(h)):
        for j in range(len(h) - 1):
            if h[j] > h[j+1]:
                h[j], h[j+1] = h[j+1], h[j]
                
def Ordem(vetor,d,h):
    d=int(input("posição do numero que quer mudar:"))
    c=int(input("posição do número com qual voce deseja trocar:"))
    vetor[d],vetor[c] = vetor[c],vetor[d]

def main():
    r="S"
    while r.upper()=="S":
        ordem = 0
        d=int(input("Digite o tamanho da linha:"))
        jogador1= input("Digite o nome do Jogador 1: ")
        jogador2= input("Digite o nome do Jogador 2: ")
        ordem = decisao(jogador1,jogador2,0)
        vetor=[]*d
        geravetor(vetor,d)
        print("Esse é o vetor original:",vetor)
        entrada.write(str(d)+"-->"+str(vetor)+"\n")
        h = sorted(vetor)
        cont = 1
        if ordem == 1:
            while vetor!=h:
                cont+=1
                if cont%2==0:
                    print("vez do ",jogador1)
                else:
                    print("vez do",jogador2)
                Ordem(vetor,d,h)
                print(vetor)
            if cont%2==0:
                print(jogador1," venceu")
                saida.write(jogador1+"\n")
            else:
                print(jogador2," venceu")
                saida.write(jogador2+"\n") 
        if ordem == 2:
            while vetor!=h:
                cont+=1
                if cont%2==0:
                    print("vez do",jogador2)
                else:
                    print("vez do",jogador1)
                Ordem(vetor,d,h)
                print(vetor)
            if cont%2==0:
                print(jogador2," venceu")
                saida.write(jogador2+"\n")
            else:
                print(jogador1," venceu")
                saida.write(jogador1+"\n")           
        r=str(input("quer continuar? (S/N)")).upper()

    saida.close()
    entrada.close()
        
    print("Voce Saiu")
    return False   
main()
