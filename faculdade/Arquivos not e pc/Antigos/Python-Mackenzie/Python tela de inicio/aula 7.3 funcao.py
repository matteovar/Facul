def maximo (n1,n2):
    if n1>n2:
        maior = n1
    else:
        maior = n2
    return maior

def main():
    n1 = 5
    n2 = 6
    print(maximo(n1,n2))

main()

#ou

def maximo (n1,n2):
    if n1>n2:
        return n1
    return n2

def main():
    n1 = 5
    n2 = 6
    print(maximo(n1,n2))

main()
