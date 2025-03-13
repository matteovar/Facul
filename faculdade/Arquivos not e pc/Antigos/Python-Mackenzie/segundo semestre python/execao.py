flag = True
while flag:
    try:
        idade = int(input('Sua idade: '))
        proxima = idade + 1
        print('Ano que vem você terá', proxima, 'anos')
        flag = False
    except ValueError:
        print("Entre somente Digitos!!!")

#OU

while True:
    try:
        idade = int(input('Sua idade: '))
        proxima = idade + 1
        print('Ano que vem você terá', proxima, 'anos')
        break
    except ValueError:
        print("Entre somente Digitos!!!")
