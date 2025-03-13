valor = int(input())

while valor<=0:
    print("VALOR INVÁLIDO")
    valor = int(input())
for i in range(1,valor+1):
    if valor%i == 0:
        print(i, end = ' ')
