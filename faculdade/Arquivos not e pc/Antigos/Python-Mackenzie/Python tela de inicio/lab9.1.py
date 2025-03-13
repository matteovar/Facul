
lista = ["Lais","Felipe","Ana"]
def msg():
    print("Escolha a opcao: ")
    print("(1) Cadastrar um amigo (no final da lista)")
    print("(2) Mostrar os nomes de todos os amigos")
    print("(3) Cadastrar um amigo (no início da lista)")
    print("(4) Remover um nome")
    print("(5) Substituir um nome")
    print("(6) Mostrar o número total de amigos cadastrados")
    print("(7) Colocar os nomes dos amigos em ordem alfabética")
    print("(9) Sair do programa")

def entrada():
    selecionado = 0
    while selecionado!= 9:
        selecionado = int(input("Opção selecionada: "))
        if selecionado == 1:
            nome = input("Nome: ")
            lista.append(nome)
        elif selecionado ==2:
            print(lista)
        elif selecionado == 3:
            nome2 = input("Nome: ")
            posicaonome = int(input("Digite a posicao do nome:"))
            lista.insert(posicaonome,nome2)
        elif selecionado ==4:
            posicaonome2 = input("Digite o nome:")
            lista.remove(posicaonome2)
        elif selecionado ==5:
            posicaonome3 = int(input("Digite a posicao do nome:"))
            nome3 = input("Nome: ")
            lista[posicaonome3] = nome3
        elif selecionado ==6:
            print(len(lista))
        elif selecionado ==7:
            lista.sort()
            print(lista)
        elif selecionado==9:
            print("Saiu do programa")
            break
        else:
            if selecionado<=0 or selecionado<=10:
                selecionado = input("Valor invalido, digite novamente: ")
    print("Fim do programa")

def main():
    msg()
    entrada()

main()
    
