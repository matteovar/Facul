from random import sample
matriz=[]
n=5

def bingo(matriz):
    for i in range(n):
        linha=[]
        for j in range(n):
            linha=sample(range(0,99),5)
        matriz.append(linha)
    return matriz

def comparar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=" ")
        print("\n")
            
def main():
    bingo(matriz)
    comparar(matriz)    
    
main()
    
            
