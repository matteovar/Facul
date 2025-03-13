def perguntas(vetor):
    print("Digite 1 se voce ja fez isso:")
    cont=0
    for i in range(len(vetor)):
        print(vetor[i])
        resposta=int(input("Resposta:"))
        if resposta==1:
            cont+=1

    if cont<2:
        print("Inocente")
    elif cont==2:
        print("Suspeito")
    elif 3<=cont<=4:
        print("Cumplice")
    else:
        print("Asssasino")

    return vetor,cont

def main():
    vetor=["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Tinha dívidas com a vítima?","Já trabalhou com a vítima?"]
    perguntas(vetor)
main()
    
