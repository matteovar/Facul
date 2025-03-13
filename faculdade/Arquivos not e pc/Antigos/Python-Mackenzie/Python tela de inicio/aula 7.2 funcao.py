def msg ():
   print("Digite suas notas")

def entrada():
    n = int(input("Numeros: "))
    while n<0:
            n = int(input("Invalido. Numeros: "))
    return n

def media (n1,n2,n3):
    total = n1+n2+n3
    return  total/3.0


def main():
    msg()
    n1 = entrada()
    n2 = entrada()
    n3 = entrada()
    print(media (n1,n2,n3))

main()
