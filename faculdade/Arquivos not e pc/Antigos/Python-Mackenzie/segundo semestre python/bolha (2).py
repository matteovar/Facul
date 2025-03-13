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

def imprime(vetor):
    for i in range(len(vetor)):
        print(vetor[i],end=" ")
    print("\n")
    
def ordem(vetor,d,h):
    d=int(input("posição do numero que quer mudar:"))
    c=int(input("posição do número com qual voce deseja trocar:"))
    vetor[d],vetor[c] = vetor[c],vetor[d]

def main():
    r="S"
    while r=="S":
        d=int(input("Digite o tamanho da linha:"))
        jogador1= input("Digite o nome do Jogador 1: ")
        jogador2= input("Digite o nome do Jogador 2: ")    
        vetor=[]*d
        geravetor(vetor,d)
        print("Esse é o vetor original:",vetor)
        entrada.write(str(d)+"-->"+str(vetor)+"\n")
        h=sorted(vetor)
        cont = 1
        while vetor!=h:
            cont+=1
            if cont%2==0:
                print("vez do ",jogador1)
            else:
                print("vez do",jogador2)
            ordem(vetor,d,h)
            print(vetor)
        if cont%2==0:
            print(jogador1," venceu")
            saida.write(jogador1+"\n")
        else:
            print(jogador2," venceu")
            saida.write(jogador2+"\n")
        r=str(input("quer continuar? (S/N)")).upper()

    saida.close()
    entrada.close()
        
    print("Voce Saiu")
    return False   
main()
