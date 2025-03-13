def area(n1,n2):
    area = (n1*n2)/2
    return area

def entrada():
    n = int (input())
    return n

def main():
    print("Base e altura: ")
    n1 =  entrada()
    n2 = entrada()
    print(area(n1,n2))
    

main()
