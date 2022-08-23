from email.errors import InvalidDateDefect


class jogador:
    def __init__(self, nome, posicao, datanasc, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao 
        self.datanasc = datanasc  
        self.nacionalidade = nacionalidade 
        self.altura = altura 
        self.peso = peso  




    def imprime(self):
        print(f" Nome: {self.nome}\n Posicao: {self.posicao}\n Data_de_nascimento: {self.datanasc}\n nacionalidade: {self.nacionalidade}\n Altura: {self.altura}\n Peso: {self.peso}")


    def idade(self, ano):
        idade = ano - self.datanasc 
        print(f"O jogador tem {idade} anos!")
    

    def aposentar(self, ano):
        idade = ano - self.datanasc 
        if self.posicao == "defesa":
            if idade >= 40:
                print("Chegou a hora de aposentar.")
            else:
                print("Ainda tem tempo para você jogar!")
                aposentar = 40 - idade 
                print(f"Falta {aposentar} ano(s) para você se aposentar!")
        if self.posicao == "meia-campo":
            if idade >= 38: 
                print("Chegou a hora de se aposentar!")
            else: 
                print("Ainda tem tempo para você jogar!")
                aposentar = 38 - idade 
                print(f"Falta {aposentar} ano(s) para você se aposentar!")
        if self.posicao == "atacante":
            if idade >= 35:
                print("Chegou a hora de sua aposentadoria.")
            else:
                print("Você ainda tem tempo para jogar!") 
                aposentar = 35 - idade 
                print(f"Falta {aposentar} ano(s) para você se aposentar!")
        else:
            print("Está opção não existe!")                                    

p1 = jogador("Daniel", "atacante", 2005, "brasileiro", 1.80, 55)


p1.imprime()
p1.idade(2022)
p1.aposentar(2039)

