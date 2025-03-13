import collections

meu_arquivo = open('letra.txt','r',encoding="utf8")
final = open("resultado.txt","w")


data = meu_arquivo.read()
data=data.replace('Ã','A')
data=data.replace('Á','A')
data=data.replace('Ç','C')
data=data.replace('\n','')
data=data.replace('-','')
data=data.replace('Í','I')
data=data.replace('(','')
data=data.replace(')','')
data=data.replace(':','')
data=data.replace(' ','')
data=data.replace('É','')
data=data.replace(',','')
data=data.replace('.','')

count = {}
for x in data:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1

for x in count.keys():
    final.write(f'letra:{x} aparece:{count[x]}\n')

final.close()
