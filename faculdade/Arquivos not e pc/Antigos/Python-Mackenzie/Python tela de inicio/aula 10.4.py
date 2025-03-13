def valorPagamento(valor,dias):
    if dias==0:
       valor
       return valor
    else:
       total= valor+(valor*0.03)+(valor*0.001)*dias
    return total
	
def main():
    valor = float(input())
    dias = int(input())
    print(valorPagamento(valor,dias))
main()

