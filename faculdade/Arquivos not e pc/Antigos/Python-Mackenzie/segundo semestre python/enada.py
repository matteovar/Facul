def pot(b, p):
    y = b ** p
    return y

def quadrado(x):
    a = pot(x, 2)
    return a

n = 5
resultado = quadrado(n)
print(resultado)
