import math
#1
n1 = float(input('digite sua nota do primeiro bimestre:'))
n2 = float(input('digite sua nota do segundo bimestre:'))
n3 = float(input('digite sua nota do terceiro bimestre:'))
n4 = float(input('digite sua nota do quarto bimestre:'))
final = (n1+n2+n3+n3/4)
print ('a media dos bimestres =', final)



#2
metros = float(input('Digite a quantos metros:'))

print ('A quantidade em metros', metros, ' convertida em milimetros é',float(metros *1000), 'milimetros')

#3
raio = float(input('Digite o raio da circunferencia:'))
area = (math.pi*raio)
print ('A area da circunferencia total foi de:', area)


#4
area = float(input('Digite o lado do quadrado:'))
lado = area*area
print ('A area do quadrado é', lado)

print ('O dobro da area do quadrado é', float(lado*2))

#5
dinheiro = float(input('Quanto voce ganha por hora?: '))
horas = float(input('Quantas horas voce trabalha no mes?: '))
horas_totais = horas * dinheiro
print ('O seu salario no mes foi de $', horas_totais, 'reais')
