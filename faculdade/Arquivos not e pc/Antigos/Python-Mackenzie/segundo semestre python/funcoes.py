def mult(a, b):
    c = 0
    cont = 0
    while b>cont:
        c += a
        cont += 1
    return c
    
    
#--------------------------->

def potencia(x,y):
    c = 1
    cont = 1
    for i in range(y):
        c *= x
        cont += 1
    return c

#--------------------------->
def ehPrimo(n1,n2):
    x = 1
    y = 0
    for x in range(n1,n2+1):
        for i in range(2, y):
            resto=(y%i)
            if y!=i and y != 1 and resto !=0:
                x += resto
            else:
                x = 0
                break
        if x>0 or y==2:
            print(y, end =" ")
        y+=1

#--------------------------->
def funcao(n):
    s = 1
    conta = int(n)
    for i in range(2, conta+1):
        if i%2 ==0:
            s=s-i/(i*i)
        if i%2 != 0:
            s=s+1
    return s
