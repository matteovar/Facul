def main():

    programa_rodando=True
    while programa_rodando:

        # imprime opções
        ...
        # pede entrada do usuario
        entrada = input()

        if entrada = "a":
            polinomio = pedir_polinomio()
            resposta = resolver_polinomio(polinomio)
            print(resposta)
        elif entrada = "b":
            polinomio1 = pedir_polinomio()
            polinomio2 = pedir_polinomio()
            resposta = somar_polinomio(polinomio1, polinomio2)
            print(resposta)
        elif entrada = "c":
            programa_rodando = False
        

main()
