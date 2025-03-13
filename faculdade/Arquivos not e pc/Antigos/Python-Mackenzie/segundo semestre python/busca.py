import random
    
def busca(v,x):
    cont=0
    for i in range(len(v)):
        cont+=1
        if v[i] == x:
            print("quantidade de passos--> ",cont)
            return i
    print("quantidade de passos--> ",cont)
    return -1;

def buscaSequencialOrdenada(v,x):    
    for i in range(len(v)):        
        if v[i] == x:
            print("quantidade de passos--> ",i+1)
            return i
        else:
            if x < v[i]:
                print("quantidade de passos--> ",i+1)
                return -1
    print("quantidade de passos--> ",i+1)    
    return -1


v=[61, 174, 197, 217, 309, 448, 503, 557, 629, 701, 831]
print("so",buscaSequencialOrdenada(v,3))
print("so",buscaSequencialOrdenada(v,25))
print("so",buscaSequencialOrdenada(v,70))

print("o",busca(v,61))
print("o",busca(v,503))

