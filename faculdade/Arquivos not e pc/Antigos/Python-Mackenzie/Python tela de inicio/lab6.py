
print ("Escolha uma das opcaoes a baxio(digitar o numero 0, ira acabar o programa)")
print ("Soma .................... +")
print ("Subtração ............. -")
print ("Multiplicação......... *")
print ("Divisão................... /")
print ("Sair ....................... 0")
n = input("Digite a opcao:")
while n != "0":
    num1 = int(input("Digite um numero:"))
    num2 = int(input("Digite outro numero:"))
    if n == "+":
        print("a soma deu",num1+num2)
    elif n =="-":
        print("a subtracao deu",num1-num2)
    elif n=="/":
        print("a divisao deu",num1/num2)
    elif n=="*":
        print(" a multiplicacao deu",num1*num2)
    else:
        print ("Voce saiu")
    n = input("Digite outra opcao:")
print ("Voce saiu")

#2
n = int(input("Digite o numero: "))
i = 0
while (i<n):
    j=0
    while (j<=i):
        print(j,end=" ")
        j+=1
    print()
    i+=1


#3
n = int(input("Digite o numero: "))
i = 0
while (i<n):
    j=0
    while (j<n-i):
        print(j,end=" ")
        j+=1
    print()    
    i+=1
    
