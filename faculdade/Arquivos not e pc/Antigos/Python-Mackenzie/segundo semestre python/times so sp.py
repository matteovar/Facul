times_arquivo = open('times_campeonato.txt', 'r')
times_sp_arquivo = open('timessp.txt', 'w')

for linha in times_arquivo:
    registro_time = linha.rstrip()
    info_time = registro_time.split(':')
    nome = info_time[0]
    estado = info_time[1]
    if estado == 'sp':
        times_sp_arquivo.write(nome+'\n')
    print(linha)
times_arquivo.close()
times_sp_arquivo.close()
#-----------------------------
