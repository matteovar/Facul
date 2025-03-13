quantidade_produtos = int(input('Quantidade de produtos na lista: '))

meu_arquivo = open('itens_pedido.txt','w', encoding="utf8")


for cont in  range(quantidade_produtos):
    quantidade = int(input('Volume do mesmo produto ' + str(cont+1) + ' : ' ))
    preco = int(input('Preco do produto ' + str(cont+1) + ' : '))
    produto = str(input('Nome do produto ' + str(cont+1) + ' : '))
    meu_arquivo.write(f'{quantidade}:{preco}:{produto} \n')
    




meu_arquivo.close()
