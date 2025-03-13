#usar n!
# n! = n*(n-1)*(n-2)....
import funcoes
a= int(input('Digite a: '))
b=int(input('Digite b: '))

print('A multiplicacao:', funcoes.mult(a, b))

#--------------------->

x= int(input("Digite o valor de x: "))
y= int(input("Digite o valor de y: "))

print(funcoes.potencia(x,y))

#--------------------->
n1 = int(input("Valor do n1: "))
n2= int(input("Valor do n2: "))

print(funcoes.ehPrimo(n1,n2))

#--------------------->
n = int(input("Valor do N: "))

print(int(funcoes.funcao(n)))
