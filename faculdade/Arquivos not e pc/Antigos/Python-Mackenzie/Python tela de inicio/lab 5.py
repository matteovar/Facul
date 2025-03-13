import random
usuario = int(input("Adivinhe o numero:"))
dado = random.randint(1,6)
print (dado)
if usuario == dado:
    print ("Parabéns, você acertou")
elif usuario<dado:
    print ("Seu palpite foi muito baixo.")
elif usuario>dado and usuario<6:
    print ("Seu palpite foi muito alto.")
elif usuario>6:
    print ("Entrada inválida!")


print( "Bem Vindo a entrada")
print ("Vai para onde agora?")
print ("Aperte 1 para ir a SALA")
print ("Aperte 2 para ir COZINHA")
opcao = input("Escolha:")
if opcao == "1":
    proximo = "SALA"
else:
    proximo = "COZINHA"

if proximo == "SALA":
    print ("Bem vindo a SALA")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a QUARTO")
    print ("Aperte 2 para ir COPA")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "QUARTO"
    else:
        proximo = "COPA"

if proximo == "COZINHA":
    print ("Bem vindo a COZINHA")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a COPA")
    print ("Aperte 2 para ir QUINTAL")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "COPA"
    else:
        proximo = "QUINTAL"
if proximo == "COPA":
    print ("Bem vindo a COPA")
    print ("Aperte 1 para ir a QUINTAL")
    opcao = input("Escolha:")
    proximo = "QUINTAL"

if proximo == "QUARTO":
    print ("Bem vindo ao QUARTO")
    print ("Aperte 1 para ir a QUINTAL")
    opcao = input("Escolha:")
    proximo = "QUINTAL"

if proximo == "QUINTAL":
    print("Bem vindo ao QUINTAL")




armadura = 20
espada = 10
escudo = 5
lanca = 15
capacete = 5


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
    print ("Que sorte, você encontrou uma ARMADURA")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a SUITE REAL")
    print ("Aperte 2 para ir CALABOUÇO")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "SUITE REAL"
    else:
        proximo = "CALABOUÇO"
    soma = soma+armadura
    

if proximo == "SUITE REAL":
    print ("Bem vindo a SUITE REAL")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a PATIO")
    opcao = input("Escolha:")
    proximo = "PATIO"

if proximo == "SALAO DE FESTAS":
    print ("Bem vindo ao SALAO DE FESTAS")
    print ("Que sorte, você encontrou uma ESCUDO")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir ao CALABOUÇO")
    print ("Aperte 2 para ir a MASMORRA")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "CALABOUÇO"
    else:
        proximo = "MASMORRA"

    soma = soma + escudo

if proximo == "CALABOUÇO":
    print ("Bem vindo a CALABOUÇO")
    print ("Que sorte, você encontrou uma ESPADA")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir ao PATIO")
    opcao = input("Escolha: ")
    proximo = "PATIO"
    soma = soma + espada
    

if proximo == "MASMORRA":
    print("Bem vindo a MASMORRA")
    print ("Que sorte, você encontrou uma LANÇA")
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a PATIO")
    opcao = input("Escolha:")
    proximo = "PATIO"
    soma = soma + lanca
   
if proximo == "PATIO":
    print ("Bem vindo ao PATIO")
    print ("Que sorte, você encontrou uma CAPACETE")
    print ("Aperte 1 para ir a TORRE")
    opcao = input("Escolha:")
    proximo = "TORRE"
    soma = soma + capacete

if proximo == "TORRE":
    print ("Bem vindo a TORRE")

print ("Neste tour você conseguiu",soma,"pontos")


import random
lista = ("espada","capacete","armadura","escudo","lanca")
equipamento = random.choice(lista)
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
    print ("Que sorte, você encontrou um", random.choice(lista))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a SUITE REAL")
    print ("Aperte 2 para ir CALABOUÇO")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "SUITE REAL"
    else:
        proximo = "CALABOUÇO"
    if random.choice(lista) == "armadura":
        soma = soma + 20
    elif random.choice(lista) == "espada":
        soma = soma + 10
    elif random.choice(lista) == "lanca":
        soma = soma+ 15
    elif random.choice(lista) == "esudo":
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
    print ("Que sorte, você encontrou um", random.choice(lista))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir ao CALABOUÇO")
    print ("Aperte 2 para ir a MASMORRA")
    opcao = input("Escolha:")
    if opcao == "1":
        proximo = "CALABOUÇO"
    else:
        proximo = "MASMORRA"
    if random.choice(lista) == "armadura":
        soma = soma + 20
    elif random.choice(lista) == "espada":
        soma = soma + 10
    elif random.choice(lista) == "lanca":
        soma = soma+ 15
    elif random.choice(lista) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
        

    
if proximo == "CALABOUÇO":
    print ("Bem vindo a CALABOUÇO")
    print ("Que sorte, você encontrou um",random.choice(lista))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir ao PATIO")
    opcao = input("Escolha: ")
    proximo = "PATIO"
    if random.choice(lista) == "armadura":
        soma = soma + 20
    elif random.choice(lista) == "espada":
        soma = soma + 10
    elif random.choice(lista) == "lanca":
        soma = soma+ 15
    elif random.choice(lista) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
        
    

if proximo == "MASMORRA":
    print("Bem vindo a MASMORRA")
    print ("Que sorte, você encontrou uma", random.choice(lista))
    print ("Vai para onde agora?")
    print ("Aperte 1 para ir a PATIO")
    opcao = input("Escolha:")
    proximo = "PATIO"
    if random.choice(lista) == "armadura":
        soma = soma + 20
    elif random.choice(lista) == "espada":
        soma = soma + 10
    elif random.choice(lista) == "lanca":
        soma = soma+ 15
    elif random.choice(lista) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
    
   
if proximo == "PATIO":
    print ("Bem vindo ao PATIO")
    print ("Que sorte, você encontrou um", random.choice(lista))
    print ("Aperte 1 para ir a TORRE")
    opcao = input("Escolha:")
    proximo = "TORRE"
    if random.choice(lista) == "armadura":
        soma = soma + 20
    elif random.choice(lista) == "espada":
        soma = soma + 10
    elif random.choice(lista) == "lanca":
        soma = soma+ 15
    elif random.choice(lista) == "esudo":
        soma = soma + 5
    else:
        soma = soma + 5
        
if proximo == "TORRE":
    print ("Bem vindo a TORRE")

print ("Neste tour você conseguiu", soma,"pontos")
    
    
    
