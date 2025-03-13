class Pessoa:
  @property                         #deixa privado
  def nome(self):                   #define um nome
    return self._nome               #retorna o nome

  @property                         #deixa privado
  def altura(self):                 #define a altura
    return self._altura             #retorna a altura

  @nome.setter                      #seta o nome
  def nome(self, n):                #define o nome como n
    self._nome = n          

  @altura.setter                    #seta a altura
  def altura(self, a):              # define a altura
    self._altura = a

p1 = Pessoa()                       #define pessoa como p1
p1.nome = input("Digite um nome")   #pede o nome de p1
p1.altura = float(input("Altura"))  #pede a altura de p1

p2 = Pessoa()                       #define poutra pessoa como p2
p2.nome = input("Digite um nome")   #pede o nome de p2
p2.altura = float(input("Altura"))  #pede a altura de p2

print("*******************")    
print (p1.nome)                     #print o nome de p1
print(p1.altura)                    #printa a altura de p1

print("*******************")
print (p2.nome)                     #printa o nome de p2
print(p2.altura)                    #printa a altura de p2


