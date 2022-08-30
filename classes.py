class Pessoa:  #Classe pai
    def __init__(self, nome, idade, peso):
        self.__nome = nome 
        self._peso = peso
        self.idade = idade

    def falar(self):
        print(f"{self.__nome} está Falando...")    

    def dormir(self):
        print(f"{self.__nome} está Dormindo...")    

    def get_peso(self):
        return self._peso

class Cliente(Pessoa):  #Herda dados da classe pai
    def comprar(self):
        print(f"{self.__nome} está comprando...")


class Aluno(Pessoa):
    def estudar(self):  #Func única da função
        print(f"{self.nome} está estudando...")


class Jogador(Pessoa):
    def jogar(self):
        print(f"{self.nome} está jogando...")        