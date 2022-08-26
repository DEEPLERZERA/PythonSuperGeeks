class Pessoa: #Inicializando classe
    ano_atual = 2022
    def __init__(self, nome, idade, falando = False, comendo = False):  #Variáveis
        self.nome = nome 
        self.idade = idade
        self.falando = falando 
        self.comendo = comendo

        variavel = "faca"

        print(variavel)



    #Cria func de falar
    def falar(self):
        print("Pessoa está falando...")



    #Cria func de comer
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo!")
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True     

    #Cria func de parar_comer
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo!")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    #Cria func de falar
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar pois está comendo!")
            return
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        print(f"{self.nome} está falando sobre {assunto}!")    
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return 
        print(f"{self.nome} parou de falar.")  
        self.falando = False
