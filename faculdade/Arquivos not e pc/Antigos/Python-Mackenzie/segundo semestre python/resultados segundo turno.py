meu_arquivo = open('jogos_turno_unico.txt','r', encoding="utf8")
meu_arquivo2 = open('resultados_jogos_turno_unico.txt', 'w')

for linha in meu_arquivo:
    registro_time = linha.rstrip()
    info_time = registro_time.split(':')
    time1 = info_time[0]
    time2 = info_time[1]

    print(f'Jogo {time1} X {time2}')
    gol1 = input("Numero de gols marcados pelo " + time1 +':')
    gol2 = input("Numero de gols marcados pelo " + time2 + ':')

    meu_arquivo2.write(f'{time1}:{gol1}:{time2}:{gol2} \n')

meu_arquivo.close()
meu_arquivo2.close() 
    
          

    
