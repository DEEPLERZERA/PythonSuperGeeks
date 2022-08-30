#public
#protected
#private

from classes import *

c1 = Cliente('João', 40, 70) #Instancia a classe Cliente
#print(c1.__nome)  #Variável privada da erro
c1.falar() #Chama a função falar da classe Cliente 

print(c1.idade) #Variável pública pode ser acessada

p1 = Pessoa('João', 20, 60) #Instancia a classe Pessoa

p1.falar() #Chama a função falar da classe Pessoa

print(p1.get_peso()) #Chama a função get_peso da classe Pessoa

print(p1._peso) #Variável protected pode ser acessada
print(c1._peso)