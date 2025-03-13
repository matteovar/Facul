
def menu():
    print("Calculadora")
    print("Selecione uma opcao:")
    print("1-Solucao do polinomio")
    print("2-Somar dois polinomio:")
    print("3-Para sair")

    opcao=int(input("Opcao:"))

    try:
        if opcao >= 0 and opcao <= 5:
            return(opcao)
        else:
            print("Opcao incorreta, por favor digite novamente")
            return(int(input("Opción: ")))
    except:
        print("Opcao incorreta, por favor digite novamente")
        return(int(input("Opción: ")))
    
def soma(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la suma de los dos polinomios
        '''
        may = x
        men = y
        sum = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = y
        sum = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        sum = sum + aux

        print("--------------------------------------------------------------")
        print("El resultado de sumar ", str(x), "+", str(y), " es: ", str(sum))
        print("--------------------------------------------------------------")
    


def main():
    while(True):
        opcion = menu()

        if opcion == 3:
            print("Fim")
            break

        else:num11 = int(input("Polinomio da primeira equacao: ")) 
            num22 = int(input("Polinomio da segunda equacao: "))

            num1=int(input("Coeficiente da primeira equacao: "))
            num2 = int(input("Elementos da segunda equacao: "))

            if opcion == 1:
                total(num1,num2)
            elif opcion == 2:
                soma(num1,num2)
            else:
                print("Opcao incorreta, por favor digite novamente")
    
main()
