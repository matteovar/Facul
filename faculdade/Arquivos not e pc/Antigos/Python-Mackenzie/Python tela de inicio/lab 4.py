print ("Digite seu salario:")
salario = float(input())
if salario<=1045.00:
    print ("O valor recolhido sera de R$", salario*0.07,'reais')
    
elif salario<=2089.60 and salario>=1045.01:
       print ("O valor recolhido sera de R$",salario*0.07+((salario-1045.00)*0.09),'reais')
       
elif salario<=3134.40 and salario>=2089.61:
    print ("O valor recolhido sera de R$",salario*0.07+((salario-1045.00)*0.09)+((salario-2089.00)*0.12),'reais')
    
elif salario<=6101.06 and salario>=3134.41:
    print ("O valor recolhido sera de R$",salario*0.07+((salario-1045.00)*0.09)+((salario-2089.00)*0.12)+((salario-3134.40)*0.14),'reais')
    
else:
    print ("O valor recolhido sera de R$",salario*0.07+((salario-1045.00)*0.09)+((salario-2089.00)*0.12)+((salario-3134.40)*0.14),'reais')



print("Digite seu salario e quantos independentes tem:")
salario = float(input())
independentes = int(input())
valor_base1 = salario-(salario*0.07)-(independentes*179.71)
valor_base2 = salario-(salario*0.07)+((salario-1045.00)*0.09)-(independentes*179.71)
valor_base3 = salario-(salario*0.07)+((salario-1045.00)*0.09)+((salario-2089.00)*0.12)-(independentes*179.71)
valor_base4 = salario-(salario*0.07)+((salario-1045.00)*0.09)+((salario-2089.00)*0.12)+((salario-3134.40)*0.14)-(independentes*179.71)
valor_base5 = salario-(salario*0.07)+((salario-1045.00)*0.09)+((salario-2089.00)*0.12)+((salario-3134.40)*0.14)-(independentes*179.71)
if salario<=1903.98:
    print (" o valor retido sera de R$",valor_base1,"reais")
    
elif salario<=2826.65 and salario>=1903.99:
    print (" o valor retido sera de R$",valor_base2*0.075-142.80,"reais")

elif salario<=3751.05 and salario>=2826.66:
    print("O valor retido sera de R$",valor_base3*0.15-354.80,"reais")
    
elif salario<=4664.68 and salario>=3751.06:
    print ("O valor retido sera de R$", valor_base4*0.225-636.13,"reais")
else:
    print ("O valor retido sera de R$", valor_base5*0.275-869.36,"reais")
