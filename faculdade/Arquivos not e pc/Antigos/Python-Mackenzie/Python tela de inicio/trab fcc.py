alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']   
chave = int(input("Digite a chave: "))
mensagem = input("Digite a mensagem: ")
mensagem2 = ""
for letra in mensagem:
    lugar = alfabeto.index(letra)   #o lugar da letra no alfabeto 
    nova = alfabeto[(lugar - chave)%26] #quantas casas a letra vaI andar
    mensagem2 +=nova


print(mensagem2)    #mostra a mensagem criptografado

print('*******************************************************')

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z',' ']
chave = int(input("Digite a chave: "))
mensagem = input("Digite a mensagem: ")
descriptografada = ""
for letra in mensagem:
    lugar = alfabeto.index(letra)       #o lugar da letra no alfabeto na mensagem criptografada
    nova = alfabeto[(lugar + chave)%26] #quantas casas a letra vaI andar
    
    descriptografada += nova #coloca a nova mensagem 

print(descriptografada) #mostra a mensagem descriptografado


