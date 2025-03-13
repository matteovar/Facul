def geraPiramide(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")
def main():
    n=int(input("N:"))
    geraPiramide(n)
main()
          
               
            
