total=[10,50,100,500,1000,5000,10000,50000,100000]

def buscaBinaria():
    for i in total:
        vet=range(i)
        cont=0
        while i>1:
            cont+=1
            i//=2
        print("Operacoes no pior caso:",cont+1)
        

vet=[-10,-5,-1,0,3,5,10,25,36,70]
buscaBinaria()
