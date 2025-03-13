num = int(input('Numero:'))

if num>=1 and num<=100:
    print( 'O valor entre 1 e 100')
else:
    print('O valor ta fora fdp, é so dentro do valor')
print('Acabou =)')




##  ex2:
print('Digite dois numeros')
num = float(input())
num1 = float(input())
if num>num1:
    print(num**2)
else:
    print(num1**2)


## ex3:
n = int(input('Numero:'))
if n%2 ==0:
    print('o numero', n , 'é par')
else:
    print ('o numero', n ,'é impar')


## ex4:
preco = float(input('Preco do Produto:'))
if preco<20.00:
    npreco = preco*1.45
else:
    npreco = preco*1.30
print('O produto sera vendido por',preco,'e sera comprado por',npreco)
