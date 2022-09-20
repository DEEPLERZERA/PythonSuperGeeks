import json

class Bot:
    def __init__(self, nome):
        try: # Tenta executar o código
            memoria = open(nome+'.json', 'r') # Abre o arquivo de memória
        except FileNotFoundError: # Se não existir
            memoria = open(nome+'.json', 'w') # Cria o arquivo de memória
            memoria.write('["Andrew"]') # Escreve a lista de conhecidos
            memoria.close() # Fecha o arquivo de memória
            memoria = open(nome+'.json', 'r') # Abre o arquivo de memória

        self.nome = nome # Nome do bot
        self.conhecidos = json.load(memoria) # Carrega o arquivo de memória
        memoria.close() # Fecha o arquivo de memória
        self.historico = [""] # Lista de frases ditas
        self.perguntaNome = ["Olá, qual é o seu nome?", "Olá, eu estou bem! Qual é o seu nome?"] # Lista de perguntas
        self.frases = {'oi': "Olá, qual é o seu nome?", "tchau": "Tchau, até mais!", "bom dia": "Bom dia!", "ola": "Olá, qual é o seu nome?", "oi, tudo bem?": "Olá, eu estou bem! Qual é o seu nome?"} # Dicionário de frases
        
    def escuta(self):
        frase = input(">: ")
        frase = frase.lower() # Deixa a frase em minúsculo
        frase = frase.replace("eh", "é") # Substitui "eh" por "é"
        frase = frase.replace('á', 'a') # Substitui "á" por "a"
        return frase # Retorna a frase  

    def pensa(self, frase):
        if frase in self.frases: # Se a frase estiver no dicionário
            return self.frases[frase] # Retorna a frase   

        if frase == "aprende": # Se a frase for aprende
            chave = input("Digite a frase: ") # Pergunta a frase
            chave = chave.lower() # Deixa a frase em minúsculo
            resp = input("Digite a resposta: ") # Pergunta a resposta
            self.frases[chave] = resp # Adiciona a frase e a resposta no dicionário
            return "Aprendido!"    # Retorna a mensagem de aprendido

        if self.historico[-1] in self.perguntaNome: # Se a última frase dita for uma pergunta de nome
            nome = self.pegaNome(frase) # Chama a função pegaNome
            resp = self.respondeNome(nome) # Chama a função respondeNome
            return resp  # Retorna a resposta

           
        try: # Tenta executar o código
            resp = str(eval(frase)) # Tenta executar a frase como código
            return resp # Retorna a resposta
        except: # Se não conseguir
            return "Não entendi!" # Retorna a mensagem de não entendido
          


    def pegaNome(self, nome): #Cria a função pegaNome
        if 'o meu nome é' in nome: # Se a frase conter "o meu nome é"
            nome = nome[13:] # Pega o nome depois de "o meu nome é"

        if 'O meu nome é' in nome: # Se a frase conter "O meu nome é"
            nome = nome[13:] # Pega o nome depois de "O meu nome é"

        if 'Eu sou o' in nome: # Se a frase conter "Eu sou o"
            nome = nome[9:]    # Pega o nome depois de "Eu sou o"

        if 'eu sou o' in nome: # Se a frase conter "eu sou o"
            nome = nome[9:]  # Pega o nome depois de "eu sou o"

        if 'Eu sou a' in nome: # Se a frase conter "Eu sou a"
            nome = nome[9:]  # Pega o nome depois de "Eu sou a"   

        if 'eu sou a' in nome: # Se a frase conter "eu sou a"
            nome = nome[9:]    # Pega o nome depois de "eu sou a"                
        return nome #Retorna o nome 

    def respondeNome(self, nome):     #Cria a função respondeNome    

        
        if nome in self.conhecidos:
            frase = "Aoba pia! "

        else:
            frase = "Muito prazer "
            self.conhecidos.append(nome)
            memoria = open(self.nome+'.json', 'w') # Abre o arquivo de memória
            json.dump(self.conhecidos, memoria) # Salva a lista de conhecidos
            memoria.close() # Fecha o arquivo de memória

        return frase + nome #Retorna a frase com o nome


    def fala(self, frase):
        print(frase)
        self.historico.append(frase) # Adiciona a frase na lista de histórico