num = 1

while(num <=3 ):
    print("digite o numero", num, ":")
    valor = int(input())
    if ((valor % 2) == 0):
        print ("o numero", valor, "é par")
    else:
        print ("numero", valor,"é impar")
    num = num + 1
print ("FIM")


#Escrever numeros de 50 a 100
import time
x = int(input())
while x<=100:
    print (x, end = ",")
    x  += 1
    time.sleep(0)
print ("\nacabou")

print (f'o valor de x fora do laco é {x}')


#fazer um programa que receba varios numeros, encerra a entrada de dacdos com -1


n = 0
while n != -1:
    n = int(input())
    if n != -1:
        print("Invalido")
    else:
        print ("acabou a entrada de numero")
        break




#fazer um programa que diminua 1, chegando ate 0
import time
x = 10
while x>=0:
    if x != 0:
        print (x, end = ',')  #end = ele fica na mesma linha
    else:
        print(x, end = "")
    x -= 1
    time.sleep (1)
print(" e lancar")
                                    # = x + 1                   x += 1



