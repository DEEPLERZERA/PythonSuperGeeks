class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso 
        self.altura = altura 



    def envelhecer(self, idade):
        self.idade +=  idade
        print(f"{self.nome} você envelheceu {idade} anos e agora tem {self.idade} anos!")

    def engordar(self, peso):
        self.peso += peso 
        print(f"{self.nome} você engordou {peso} kilos e agora pesa {self.peso} kilos!")    


    def emagrecer(self, peso):
        self.peso -=  peso 
        print(f"{self.nome} você emagreceu {peso} kilos e agora pesa {self.peso} kilos!")    
       

    def crescer(self, altura):
        self.altura += altura 
        print(f"{self.nome} você cresceu {altura} centimetros e  agora está com tamanho de {self.altura}!")    





p1 = Pessoa("daniel", 10, 55, 1.80)

p1.envelhecer(2)
p1.engordar(5)
p1.emagrecer(5)
p1.crescer(0.10)



