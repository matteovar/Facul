'''
m= int(input("Digite o grau da equacao:"))
x=int(input("Valor de x:"))
vetor=[0]*(m+1)

result=0
def polinomio(vetor):
    for i in range(m+1):
        n= int(input("Digite o coeficiente"+str(i+1)+":"))
        vetor[i]=n
    return vetor


def polinomio2(result):   
    for i in range(len(vetor)):
        sum=vetor[i]
    
        for j in range(len(vetor)-i-1):
            sum*=x
        result += sum
    return result

print(polinomio(vetor))
print(polinomio2(result))

z=int(input("Digite o grau da equacao1:"))
x=int(input("Digite o grau da equacao2:"))

def vetorA(A):
    for i in range(z+1):
        c= int(input("Digite o coeficiente"+str(i+1)+":"))
        A[i]=c
    return A
def vetorB(B):
    for j in range(x+1):
        v=int(input("Digite o coeficiente"+str(j+1)+":"))
        B[j]=v
    return B
def add(A, B, m, n):

    size = max(m, n);
    sum = [0 for i in range(size)]

    
    for i in range(0, m, 1):
        sum[i] = A[i]


    for i in range(n):
        sum[i] += B[i]

    return sum

def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")

# Driver Code

    
    
A = [0]*(z+1)   
B = [0]*(x+1)
m = len(A)
n = len(B)
vetorA(A)
vetorB(B)
print("First polynomial is")
printPoly(A, m)
print("\n", end = "")
print("Second polynomial is")
printPoly(B, n)
print("\n", end = "")
sum = add(A, B, m, n)
size = max(m, n)

print("sum polynomial is")
printPoly(sum, size)
'''
def suma(self, x, y):
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
    
