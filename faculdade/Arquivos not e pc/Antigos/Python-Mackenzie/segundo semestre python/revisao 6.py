import random


def geraMatriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(10):
            linha.append(random.choice("abcd"))
        matriz.append(linha)
    return matriz

def gabarito():
    gaba = []
    for j in range(10):
        gaba.append(random.choice('abcd'))
    return gaba

def resultado(matriz, gaba):
    resultado = [0]*5
    for i in range(5):
        for j in range(10):
            if matriz[i][j] == gaba[j]:
                resultado[i] +=1
    return resultado 
            
    
def main():
    notas = geraMatriz()
    gab= gabarito()
    result = resultado(notas,gab)
    for i in range(5):
        print('\nAlunos',i, notas[i],end = ' ')
    print('')
    print('Gabarito:',gab)
    print('\nResultados:',result,)
          
        
main()
