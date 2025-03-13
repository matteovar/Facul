turma = int(input())

soma = 0
for i in range (turma):
    i = float(input())
    if i>=6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    soma+=i
    

if turma ==0:
    print("NÃO HOUVE PROCESSAMENTO")
else:
    total = soma/turma
    print(total)
    


            
        
    
