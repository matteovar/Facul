
def notas(vetor):
    for i in range(len(vetor)):
        n=int(input("Digite as notas:"))
        vetor[i]=n
    return vetor


def media(vetor):
    soma=0
    for i in range(len(vetor)):
        soma = soma+vetor[i] 
    media = soma/len(vetor)
    print('soma:',soma,"\nMedia",media)
    return media


def maiormedia(vetor,media):
    for i in range(len(vetor)):
        if media<=vetor[i]:
            print(vetor[i],"--Acimma da media")
        else:
            print(vetor[i],"--Abaixo")
    
def main():
    m=int(input("Digite a quantidade de notas:"))
    vetor=[0]*m
    vetor = notas(vetor)
    #print("Notas na ordem digitada:",vetor)
    #print("Notas invertidas:",vetor[::-1])
    mediaT = media(vetor)
    print(mediaT)
    maiormedia(vetor,mediaT)
main()
