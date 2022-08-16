class Pessoa:
    def __init__(self, nome, idade, falando = False, comendo = False):
        self.nome = nome 
        self.idade = idade
        self.falando = falando 
        self.comendo = comendo

        variavel = "faca"

        print(variavel)




    def falar(self):
        print("Pessoa está falando...")




    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True     


