# 1

num = int(input('Digite um numero:'))
if num>0:
    print('O numero',num, 'é positivo')
else:
    print('O numero',num,'é negativo')

# 2
print('Digite dois numeros:')
num1 = int(input())
num2 = int(input())
if num1>num2:
    print('O',num1,'é maior que',num2)
elif num1==num2 :
    print('Eles sao iguais') 
else:
    print('O', num2, 'é maior que', num1)

# 3
print('Digite dois nomes:')
name1 = str(input())
name2 = str(input())
if name1<name2:
    print(name1,name2)
else:
    print(name2,name1)

# 4
import math

num = float(input('Digite um número: '))
if num % 3 == 0 and num % 5 == 0:
    print('é divisível por 3 e por 5 ao mesmo tempo.')
else:
    print('Nao é divisivel por 3 e por 5')

#5
    import math 
print('Digite o ano:')
ano = int(input())
if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
    print('É bissexto')
else:
    print('Nao é bissexto')


#6
print ('Digite um sexo:')
sexo = input()
if sexo == "M" or "m":
    
  print("Sexo válido")
elif sexo == "F" or "f":
  print("Sexo válido")
else:
  print("Sexo inválido")

#7
  import math
print ('Digite o valor e o ano do carro:')
veiculo = float(input())
ano = int(input())
if ano < 2010:
    taxa = veiculo*1.025
    print('O valor para caros de anaos menores que 2010 é de',taxa)
else:
    taxa = veiculo*1.035
    print('Para carros maiores que 2010 é de',taxa)
    

