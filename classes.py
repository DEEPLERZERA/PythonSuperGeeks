class Pessoa:  #Classe pai
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está Falando...")    

    def dormir(self):
        print(f"{self.nome} está Dormindo...")    

class Cliente(Pessoa):  #Herda dados da classe pai
    def comprar(self):
        print(f"{self.nome} está comprando...")


class Aluno(Pessoa):
    def estudar(self):  #Func única da função
        print(f"{self.nome} está estudando...")


class Jogador(Pessoa):
    def jogar(self):
        print(f"{self.nome} está jogando...")        