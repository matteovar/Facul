def main():
    
    print('Qual o melhor Sistema Operacional para uso em servidores?')
    print('''\n1- Windows XP;
    2- Unix;
    3- Linux;
    4- Netware;
    5- Mac OS;
    6- Outro''')

    ops = ['Windows XP','Unix','Linux','Netware','Mac OS','Outro']
    sis_op = [0]*6
    while True:
        while True:
            opes = int(input('Digite a opção: '))
            if opes > 6 or opes < 0:
                print('Opção inválida.')
            else:
                break
        if opes == 0:
            break
        sis_op[opes - 1] = sis_op[opes - 1] + 1

    print('Sistema Operacional     Votos  %')
    print('----------------------------------')
    cont = 0
    melhor = 0
    melhorSis = ''
    perc = 0
    for s in sis_op:
        print('%s   %d   %.2f%%' % (ops[cont], s,(s * 100) / sum(sis_op) ))
        if s > melhor:
            melhor = s
            melhorSis = ops[cont]
            perc = (s * 100) / sum(sis_op)
        elif s == melhor:
            melhor = s
            melhorSis += ' e ' + ops[cont]
        cont += 1
        

    print('----------------------------------')
    print('Total ',sum(sis_op))
    print('O Sistema Operacional mais votado foi o', melhorSis,' com ' ,melhor, 'votos, correspondendo a', perc, 'dos votos.')




    
main()
