def entrada():
    n = int(input("Numero desejad: "))
    return n

def qtde_primos(n1):
    for i in range(1, n1 +1):
        if (i>1):
            for h in range(2, i):
                if (i%h) == 0:
                    break
            else:
                print(i, end = ",")
  
def main():
    n1 = entrada()
    qtde_primos(n1)
    

main()
    
