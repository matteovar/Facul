        
def entrada():
    x = int(input("digite um numero para fatorar: "))
    return x

def primos(n1):
    soma = 0
    for i in range(1, n1+1):
        if n1 % i ==0:
            soma += 1
    if soma ==2:
        print("eh primo")
    else:
        print("nao eh primo")
    return i

        
def main():
    n1 = entrada()
    primos(n1)

main()
