import random
lista = ("espada","capacete","armadura","escudo","lanca")
equipamento = random.sample(lista,k=1)
print(equipamento)


soma = 0


print( "Bem Vindo a PORTAO")
print ("Vai para onde agora?")
print ("Aperte 1 para ir a SALA DO TRONO")
print ("Aperte 2 para ir SALAO DE FESTAS")
opcao = input("Escolha:")
if opcao == "1":
    proximo = "SALA DO TRONO"
else:
    proximo = "SALAO DE FESTAS"


if proximo == "SALA DO TRONO":
    print ("Bem vindo a SALA DO TRONO")
    print ("Que sorte, você encontrou um", random.sample(lista,k=1))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a SUITE REAL")
    print ("Aperte 2 para ir CALABOUÇO")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "SUITE REAL"
    else:
        proximo = "CALABOUÇO"
    if random.sample(lista,k=1) == "armadura":
        soma = soma + 20
    elif random.sample(lista,k=1) == "espada":
        soma = soma + 10
    elif random.sample(lista,k=1) == "lanca":
        soma = soma+ 15
    elif random.sample(lista,k=1) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
    
    

if proximo == "SUITE REAL":
    print ("Bem vindo a SUITE REAL")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a PATIO")
    opcao = input("Escolha:")
    proximo = "PATIO"

if proximo == "SALAO DE FESTAS":
    print ("Bem vindo ao SALAO DE FESTAS")
    print ("Que sorte, você encontrou um", random.sample(lista,k=1))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir ao CALABOUÇO")
    print ("Aperte 2 para ir a MASMORRA")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "CALABOUÇO"
    else:
        proximo = "MASMORRA"
    if random.sample(lista,k=1) == "armadura":
        soma = soma + 20
    elif random.sample(lista,k=1) == "espada":
        soma = soma + 10
    elif random.sample(lista,k=1) == "lanca":
        soma = soma+ 15
    elif random.sample(lista,k=1) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
        

    
if proximo == "CALABOUÇO":
    print ("Bem vindo a CALABOUÇO")
    print ("Que sorte, você encontrou um" ,random.sample(lista,k=1))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir ao PATIO")
    opcao = input("Escolha: ")
    proximo = "PATIO"
    if random.sample(lista,k=1) == "armadura":
        soma = soma + 20
    elif random.sample(lista,k=1) == "espada":
        soma = soma + 10
    elif random.sample(lista,k=1) == "lanca":
        soma = soma+ 15
    elif random.sample(lista,k=1) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
        
    

if proximo == "MASMORRA":
    print("Bem vindo a MASMORRA")
    print ("Que sorte, você encontrou uma", random.sample(lista,k=1))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a PATIO")
    opcao = input("Escolha:")
    proximo = "PATIO"
    if random.sample(lista,k=1) == "armadura":
        soma = soma + 20
    elif random.sample(lista,k=1) == "espada":
        soma = soma + 10
    elif random.sample(lista,k=1) == "lanca":
        soma = soma+ 15
    elif random.sample(lista,k=1) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
    
   
if proximo == "PATIO":
    print ("Bem vindo ao PATIO")
    print ("Que sorte, você encontrou um", random.sample(lista,k=1))
    print ("Aperte 1 para ir a TORRE")
    opcao = input("Escolha:")
    proximo = "TORRE"
    if random.sample(lista,k=1) == "armadura":
        soma = soma + 20
    elif random.sample(lista,k=1) == "espada":
        soma = soma + 10
    elif random.sample(lista,k=1) == "lanca":
        soma = soma+ 15
    elif random.sample(lista,k=1) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
        
if proximo == "TORRE":
    print ("Bem vindo a TORRE")

print ("Neste tour você conseguiu", soma,"pontos")

