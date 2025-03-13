try:
    meu_arquivo = open('salario.csv ','r', encoding="utf8")
    meu_arquivo2 = open('salarios_5000.csv','w')

    for linha in meu_arquivo:
        registro_salario = linha.rstrip()
        info_salario = registro_salario.split(':')
        codigo_funcionario = info_salario[0]
        salario = float(info_salario[1])
        if salario > 5000:
            meu_arquivo2.write(f'{codigo_funcionario}:{salario} \n')

    meu_arquivo.close()
    meu_arquivo2.close()

except FileNotFoundError:
    print('O arquivo',meu_arquivo,'nao foi encontrado')
