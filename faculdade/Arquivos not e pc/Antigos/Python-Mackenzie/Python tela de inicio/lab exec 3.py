#ex1
print (" Digite o preco da etiqueta :")
preco = float(input("preco da etiqueta:"))
print ("Selecione o tipo de pagamento:")
print ("Digite 1 para dinheiro")
print ("Digite 2 para cartao de credito")
print ("Digite 3 para 2 vezes sem juros")
print ("Digite 4 para 3 vezes maais juros de 10%")
pagamento = int(input("tipo de pagamento:"))
if pagamento == 1:
    print ("O total foi de", preco * 0.9,"reais")
elif pagamento ==2:
    print ("O total foi de", preco * 0.95, "reais")
elif pagamento == 3:
    print ("O total foi de", preco/2,"reais")
else:
    print("O total foi de", preco*1.10/3,"reais")


#ex2
print ("Responda as perguntas com 1=Sim e 0=Nao")
print  ("Telefonou para a vítima?")
a = int(input())
print("Esteve no local do crime?")
b = int(input())
print ("Mora perto da vítima?")
c = int(input())
print ("Devia para a vítima?")
d = int(input())
print ("Já trabalhou com a vítima?")
e = int(input())

soma = a + b + c + d + e

if(soma < 2):
    print("Inocente")
elif(soma == 2):
    print("Suspeita")
elif(3 >= soma):
    print("Cúmplice")
elif(soma == 5):
    print("Assassino")



#ex 3
print ("Digite o codigo da Regiao:")
print ("1=Sul,2=Norte,3=Leste,4=Oeste,5=Noroeste,6=Sudeste,7=Centro-oeste,8=Nordeste")
regiao = int(input())
print ("Nome:")
nome = str(input())
print ("Numero de pecas vendidadas:")
pecas = int(input())
print ("Nome do vendedor:")
nome = str(input())
if pecas<1000 and regiao==1:
   frete = pecas+1
elif pecas>1000 and regiao ==1:
    frete = pecas*1.10
elif pecas<1000 and regiao ==2:
    frete = pecas +1.10
elif pecas>1000 and regiao==2:
    frete = pecas*1.08
elif pecas<1000 and regiao==3:
    frete = pecas +1.15
elif pecas>1000 and regiao ==3:
    frete = pecas *1.07
elif pecas<1000 and regiao==4:
    frete = pecas +1.20
elif pecas>1000 and regiao ==4:
    frete = pecas*1.11
elif pecas<1000 and regiao ==5:
    frete= pecas+1.25
elif pecas>1000 and regiao==5:
    frete= pecas *1.15
elif pecas<1000 and regiao==6:
    frete = pecas +1.30
elif pecas>1000 and regiao==6:
    frete = pecas*1.12
elif pecas<1000 and regiao==7:
    frete = pecas+1.40
elif pecas>1000 and regiao==7:
    frete = pecas*1.18
elif pecas<1000 and regiao==8:
    frete = pecas+1.35
elif pecas>1000 and regiao==8:
    frete = pecas*1.15
valorfinal = pecas*7 + frete*1.5
print ("o valor o frete vai ser de R$",int(valorfinal),"para o nome", nome,"e regiao", regiao)
print ("a comissao do vendedor vai ser de R$", int(valorfinal*0.065))
print ("o lucro foi de R$",int(valorfinal -(pecas*7)-valorfinal*0.065))




#ex4
a = int(input("Digiti um numero ineiro:"))
b = int(input("Digite outro numero inteiro:"))
c = int(input("Digite mais um numero inteiro:"))
if a==max(a,b,c):
    a = a+c
    c = a-c
    a = a-c
elif b==max(a,b,c):
    b = b+c
    c = b-c
    b = b-c
if a > b:
    a = a+b
    print(a)
    b = a-b
    print (b)
    a = a-b
    print (a)
print ('a=', a)
print ('b=', b)
print ('c=', c)
    

