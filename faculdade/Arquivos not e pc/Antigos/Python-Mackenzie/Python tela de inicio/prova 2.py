n1 = int(input('Número 1:'))

n2 = int(input('Número 2:'))

if (n1%n2==0 and n1>n2):

    print ('N1 é divisivel por n2 e maior que n2')

elif (n2%n1==0 and n2>n1):

    print ('N2 é divisivel por n1 e maior que n1')

else:

    print('os números não atendem os requisitos acima')
