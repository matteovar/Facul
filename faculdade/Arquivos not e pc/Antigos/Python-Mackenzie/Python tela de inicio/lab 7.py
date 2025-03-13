'''
#1
for n in range(1,100,2):
    print(n)

#2
num1 = int(input("Digite um numero para fatorar: "))
fat = 1
while(num1<=0):
    num1 = int(input("Digite um numero valido para fatorar: "))
for n in range(1,num1+1):
    fat *=n
print("o fatorial de", num1,"é: ", fat)
'''  

#3
n = int(input("Digite um numero para a serie: "))
soma= 0
while(n<=0):
    n = int(input("Digite um numero valido para fatorar: "))
for i in range (1,n+1):
    soma += ((2*i)-1)/i
print("o valor da serie é", soma)
    
#4
n = int(input("Digite quantos numeros quer na sequencia: "))    #ask the number
ant = 0                     #where it starts
prox = 1                    # next number on the sequence
for i in range(0,n):        # i starts in 0 and 
    print(ant)
    prim = ant
    ant = prox
    prox += prim
    
