print ("Hello Word")

num1 = int(input("Digite um numero:"))
print ("O numero informado foi:",num1)


print ("Digite dois numeros:")
a = int(input())
b = int(input())
c = a + b
print (c)

print ("Digite suas notas bimestrais:")
bi1 = float(input("Primeiro Bimestre:"))
bi2 = float(input("Segundo Bimestre:"))
bi3 = float(input("Terceiro Bimestre:"))
bi4 = float(input("Quarto Bimestre:"))
final = bi1+bi2+bi3+bi4/4
if final<7:
    print("Voce ta de rec marreco")
else:
    print("Parabens marreco")


print("Digite o numero em metros:")
metros = float(input())
cm = metros*100
print (cm,"cm")

import math
print ("Digite o raio do circulo:")
raio = int(input())
area = int(math.pi) * (raio**2)
print ("area do circulo é", area)
                  

import math
print ("Digite o lado do quadrado:")
l1 = float(input())
l2 = l1*l1
print ("A area do quadrado é", l2)
l3 = l2**2
print ("A area elevada ao quadrado é ", l3)


print ("Digite quanto voce ganha por hora e o quantas horas trabalha no mes")
ganha = int(input())
horas = int(input())
final_do_mes = ganha * horas
print ("Voce ganha R$",final_do_mes,"no final do mes")

print("Digite a temperatura em F:")
graus  = int(input())
C = 5*((graus-32)/9)
print ("Trasformando F em C é de", C)



#(0 °C × 9/5) + 32 =

print("DIgite o C:")
C = int(input())
F = (C *9/5)+32
print("Transformando C em F é de", F)








