#rstrip()----> remove o enter
meu_arquivo = open('times.txt', 'r', encoding="utf8")

time_a = meu_arquivo.readline().rstrip()
time_b = meu_arquivo.readline()
time_c = meu_arquivo.readline().rstrip()
time_d = meu_arquivo.readlines()[2]#linha especifica

print('Jogo:')
print(time_a, 'versus', time_c)
print('Não perca este evento!')

meu_arquivo.close()

#--------------------------------------------------->
final_arquivo = False
string_vazia = ''

meu_arquivo = open('times.txt', 'r', encoding="utf8")
print('Times que participarão deste campeonato:')

while not final_arquivo:
    linha = meu_arquivo.readline()
    if linha == string_vazia:
        final_arquivo = True
    else:
        time = linha.rstrip()
        print('-', time)

meu_arquivo.close()
print('\nNão perca os jogos deste campeonato!')
#--------------------------------------------------------->
final_arquivo = False
string_vazia = ''

meu_arquivo = open('times.txt', 'r', encoding="utf8")

lista =[]
while not final_arquivo:
    linha = meu_arquivo.readline()
    if linha == string_vazia:
        final_arquivo = True
    else:
        lista.append(linha.rstrip())
        
meu_arquivo.close()

print(lista)
