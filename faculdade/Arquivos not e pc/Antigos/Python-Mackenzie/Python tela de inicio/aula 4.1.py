''' VAMo comecar a usar o elif'''

print("Digite a nota e a frequencia:      ")
nota = float(input())
frequencia = float(input())
if nota>= 7.5 and frequencia >= 0.75:
    print( 'Passo direto')
elif nota == 6.0 and frequencia ==0.75:
    print("AHH TA BANIDO, TA DE REC SEU LIXO")
else:
    print("AHHHHHHH TA MAIS BANIDO AINDA, REPROVADO PRA KRL")
    
print("Digite sua nota:")
grade = int(input())
if grade>= 90:
    print("Grade de A")
elif grade >= 80:
    print("Grande de B")
elif grade >= 70:
    print("Grade de C")
elif grade >= 60:
    print("Grade de D")
else:
    print("Grade de E")
    
''' descobrir qual o menor numero entre os 3'''

print ("Digite tres numeros")
a = int(input())
b = int(input())
c = int(input())

if a<=b and a<=c:
    print (f'{a} é menor')
elif b<=a and b<=c:
    print (f'{b} é menor')
else:
    print (f'{c} é menor')




#criar jogo de tabuleiro

import random
soma = 0
print('Primeira Jogada')
dado = random.randint (1,6)
print (dado)
soma = soma + dado
print ('Segunda Jogada')
dado = random.randint (1,6)
print (dado)
soma = soma + dado
print ('Terceira Jogada')
dado = random.randint (1,6)
print (dado)
soma = soma + dado
print ('Total = ', soma)
if soma<5:
    print ('voce se fudeo otario')
elif soma>15:
    print('ta com sorte em viado krl')
else:
    print ('VC TA COM O CU VIRADO PRA LUA')
