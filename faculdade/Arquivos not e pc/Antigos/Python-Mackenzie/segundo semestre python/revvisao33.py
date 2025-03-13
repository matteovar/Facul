import random
def criavetor(vetor1):
    for i in range(len(vetor1)):
        vetor1[i]=random.randint(1,100)
    return vetor1

def gravarquiv(vetor1):
    arquivo=open('valores.txt','w',encoding="utf8")
    for i in range(len(vetor1)):
        arquivo.write(str(vetor1[i]))
    arquivo.close()
    return arquivo

def lerarquivo(v):
    arquivo=open('valores.txt','w',encoding="utf8")
    tamanho=arquivo.readlines()
    vetor1=[0]*len(tamanho)
    for linha in arquivo:
        vetor1[i]=int(linha.rstrip())
    arquivo.close()
    return vetor1
def meno(vetor1):
    menor=0
    for i in range(len(vetor1)-1):
        if vetor1[i]<=vetor[i+1]:
            menor=vetor1[i]
    return menor

def main():
    m=int(input("Tamanho:"))
    vetor1=[0]*m
    vetor1=criavetor(vetor1)
    arquivo.write(str(vetor1))
    arquivo.close()
main()




