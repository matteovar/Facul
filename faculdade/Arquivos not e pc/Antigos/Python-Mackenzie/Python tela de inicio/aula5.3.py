print("Digite 3 numeros")
cont = 0        #contador comeca do 0
while cont<3:
    n1= int(input())
    cont += 1
print("sair")



print ("Digite varios numeros(-1 encerra):")
n=int(input())
while n!= -1:
    n = int(input())
print("saiu")


print ("Digite varios numeros(-1 encerra):")
while True:             #quando for verdadeiro 
    n = int(input())    #se repete
    if n == -1:         #mas se for -1
        break           #para o n
print("saiu")           #encerra




nota = float(input("Digite sua nota: "))                        # pede a nota
while nota<0 or nota>10:                                        # se a nota for <0 e >10, ele fala que ta errado e pede de novo
    nota = float(input("Valor invalido!!. Digite sua nota: "))  # pede a nota correta e fala que esta invalida
print("A nota digitada foi", nota)



#validando notas de n1 e n2

n1 = float(input("Digite a nota: "))
while n1<0 or n1>10:
    n1 = float(input("Digite a nota correta: "))
    
n2= float(input("Digite a nota: "))
while n2<0 or n2>10:
    n1 = float(input("Digite a nota correta: "))

total = (n1+n2)/2
print("A media foi de", total)


#repeticoes

cond = "S"
while cond.upper() != "N":          #pega a letra e coloca em maiusculo
    print ("Tamo aqui")
    print("Escreve aqui")
    cond = input("Quer seguir? (S/N)")
    while cond.upper() != "S" and cond.upper() != "N":
        print("Opcao lida", cond.upper())
        cond = input("Opcao invalida")
print("Paramos o laco")




