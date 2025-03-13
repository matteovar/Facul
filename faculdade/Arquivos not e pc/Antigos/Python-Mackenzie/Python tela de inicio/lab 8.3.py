def entrada():
    n = int(input("digite um numero para fatorar: "))
    return n

def divisao(n1):
    for i in range(1,n1+1):
        if n1%i == 0:
            print (i, end = "," )
    return i

def main():
    n1 = entrada()
    divisao(n1)

main()


            
