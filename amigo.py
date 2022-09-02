class Pessoa:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando...")

    def comer(self):
        print(f"{self.nome} está comendo...") 

    def andar(self):
        print(f"{self.nome} está andando...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

class amigo(Pessoa):
    def __init__(self, nome, sexo, idade, niver):
        super().__init__(nome, sexo, idade)
        self.niver = niver

      


c1 = Pessoa("João", "masculino", 20)  

c1.falar()
c1.comer()
c1.andar()
c1.dormir()

f1 = amigo("João", "masculino", 20, "20/10/2000") 

print(f"{f1.nome} está fazendo aniversario no dia {f1.niver}")