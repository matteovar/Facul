a = int(input())
b = int(input())
c = int(input())
if a<b and a<c:
    print (a, "'e o menor")
elif b<a and b<c:
    print (b, " 'e menor")
else:
    print (c, "é o menor.")

import math
print ("Digite os lados")
a = float(input())
if a==0:
    print("Nao é possivel pois seria uma equacao de primeiro grau")
else:
    b = float(input())
    c = float(input())
    delta = (b**2) - 4*a*c
    if delta==0:
        x1 = (-b * math.sqrt(delta))/(2*a)
        print (x1)
    elif delta<0:
        print  ("nao tem raiz")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print (x1, x2)
        





print ("Digite os lados do triangulo")
lado1 = int(input())


lado2 = int(input())
lado3 = int(input())
if a==0 and b==0 and c==0:
    print("nao da")
if lado1==lado2 and lado2==lado3:
    print("Esse é um triangulo equilatero")
elif lado1==lado2 and lado1 != lado2:
    print("'e isoceles")
elif lado1==lado2 and lado2 != lado3:
    print ("é isoceles")
elif lado1==lado3  and lado2 !=lado1:
    print ("isoceles")
elif lado1==lado3 and lado2 != lado3:
    print ("isoceles")
elif lado2==lado3 and lado1 != lado2:
    print("é isoceles")
elif lado2==lado3 and lado1 != lado3:
    print("é isoceles")
else:
    print("escaleno")


