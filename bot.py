class Bot:
    def __init__(self, nome):
        self.nome = nome # Nome do bot
        self.conhecidos = ["natalia", "gustavo", "livia", "marcelo", "rauny", "kauan", "jessica", "daniel", "ricardo", "gleidson", "william", "andrey", "fabricio", "tutão", "marcio", "sifz", "joão", "ronoilson", "gaules"] # Lista de nomes conhecidos
        self.historico = [] # Lista de frases ditas
        
    def escuta(self):
        frase = input(">: ")
        frase = frase.lower()
        frase = frase.replace("eh", "é")
        return frase # Retorna a frase  

    def pensa(self, frase):
        if frase == "oi":
            return "Olá, qual é o seu nome?"
        if self.historico[-1] == "Olá, qual é o seu nome?":
            pass

    def fala(self, frase):
        print(frase)
        self.historico.append(frase) # Adiciona a frase na lista de histórico