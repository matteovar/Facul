import math
def soma(vetor):
    total=0
    for i in vetor:
        total+=i
    return total

def media(vetor):
    media=sum(vetor)/len(vetor)
    return media

def var(vetor,media):
    media=media(vetor)
    var = sum((1-media)**2 for i in vetor)/len(vetor)
    return var

def desvio(vetor):
    return math.sqrt(var(vetor,media))
    

            

def main():
    vetor=[5,10,56,15,3,5,8,7,10,11]
    print("Soma:",soma(vetor))
    print("Media:", media(vetor))
    print("var:",var(vetor,media))
    print("Desvio:",desvio(vetor))_
    
    
     
main()
