#2
def entrada():
    n = int(input("Digite um numero para fatorar: "))
    return n

def fatorial(n1):
    soma = 1
    for i in range(1,n1+1):
        soma *= i
    return soma


def main():
    n1 = entrada()
    print(fatorial(n1))

main()
    
