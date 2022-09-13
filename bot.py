import json

class Bot:
    def __init__(self, nome):
        self.nome = nome # Nome do bot
        memoria = open(nome+'.json', 'r') # Abre o arquivo de memória
        self.conhecidos = json.load(memoria) # Carrega o arquivo de memória
        memoria.close() # Fecha o arquivo de memória
        self.historico = [""] # Lista de frases ditas
        
    def escuta(self):
        frase = input(">: ")
        frase = frase.lower()
        frase = frase.replace("eh", "é")
        return frase # Retorna a frase  

    def pensa(self, frase):
        if frase == "oi":
            return "Olá, qual é o seu nome?"

        

        if self.historico[-1] == "Olá, qual é o seu nome?":
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp 

        return "Não entendi"    


    def pegaNome(self, nome): #Cria a função pegaNome
        if 'o meu nome é' in nome:
            nome = nome[13:]

        if 'O meu nome é' in nome:
            nome = nome[13:]
        return nome #Retorna o nome 

    def respondeNome(self, nome):     #Cria a função respondeNome    

        
        if nome in self.conhecidos:
            frase = "Aoba pia! "

        else:
            frase = "Muito prazer "
            self.conhecidos.append(nome)
            memoria = open(self.nome+'.json', 'w') # Abre o arquivo de memória

        return frase + nome #Retorna a frase com o nome


    def fala(self, frase):
        print(frase)
        self.historico.append(frase) # Adiciona a frase na lista de histórico