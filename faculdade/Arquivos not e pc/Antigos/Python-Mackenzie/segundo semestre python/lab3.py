'''
Entrega do Trabalho: Polinomio- Algoritmos e Programação II
Nós,

Matteo Domiciano Varnier
Augusto Carrera

declaramos que

todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
'''
def resolver():
    e= int(input("Digite o grau da equacao:"))
    x=int(input("Valor de x:"))
    vetor=[0]*(e+1)
    result=0
    for i in range(e+1):
        n= int(input("Digite o coeficiente"+str(i+1)+":"))
        vetor[i]=n
    for i in range(len(vetor)):
        sum=vetor[i]
        for j in range(len(vetor)-i-1):
            sum*=x
        result += sum
    for i in range(len(vetor)):
        print(vetor[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")
        if (i==e):
            print('= ', end= "")
    return result
#____________________________________________________________________#
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


def main():
    programa_rodando=True
    while programa_rodando:
        print("#-------------------------------------------------------------#")
        print("   Calculadora!  ")
        print("Digite uma das opcoes a baixo")
        print("1-Para resolver a equacao:")
        print("2-Para somar")
        print("3-Para sair da calculadora")
        l= int(input("Opcao:"))
        if l ==1:
            print(resolver())
        elif l==2:
            z=int(input("Digite o grau da equacao1:"))
            x=int(input("Digite o grau da equacao2:"))
            A = [0]*(z+1)
            B = [0]*(x+1) 
            m = len(A) 
            n = len(B) 
            for i in range(z+1):
                c= int(input("Digite o coeficiente1:"))
                A[i]=c
            for i in range(x+1):
                v=int(input("Digite o coeficiente2:"))
                B[i]=v
            print("Primeiro Polinomio") 
            printPoly(A, m) 
            print("\nSegundo Polinomio") 
            printPoly(B, n)  
            sum = add(A, B, m, n) 
            size = max(m, n)
            print("\nA soma total é:") 
            printPoly(sum, size)
            print("")
        elif l ==3:
            print("Que Pena!!Voce escolheu sair")
            print("Tchau!")
            breaks
     
main()
