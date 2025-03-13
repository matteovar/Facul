#1
def intervalo(n1,n2):
    for n in range (n1,n2+1,1):
        if n%2==0:
            print(n)
    return(n)
            
def entrada():
     x = int(input("Intervalos: "))
     return x


def main():
    n1 = entrada()
    n2 = entrada()
    intervalo(n1,n2)
    

main()

