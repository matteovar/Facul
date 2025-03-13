amigos = ["Lais","Felipe","Ana"]

def msg():
    print("(1) Cadastrar um amigo (no final da lista)")
    print("(2) Mostrar os nomes de todos os amigos")
    print("(9) Sair do programa")

def entrada():
    selecionado = 0
    while selecionado != 9:
        selecionado = int(input("Opção selecionada: "))
        if selecionado ==  1 :
            nome = input("Digite o nome:")
            lst = amigos.append(nome)
        elif selecionado == 2:
            print(amigos)
        elif selecionado ==9:
            print("saiu")
            break
        else:
            if 2<selecionado<9 or selecionado<=0 or selecionado>=10:
                selecionado = input("Valor invalido, digite novamente: ")
    print("Fim do programa")
    
        
    
def main():
    msg()
    entrada()

main()


