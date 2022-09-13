from bot import Bot

bot = Bot("Andrew") # Cria o objeto bot


while True:
  frase = bot.escuta() # Escuta a frase
  resp = bot.pensa(frase) # Pensa na resposta
  bot.fala(resp) # Fala a resposta

  if frase == "tchau":
        break


print("Bye Bye!")        


#arquivo = open("historico.txt", "w") # Abre o arquivo para escrita
#arquivo.write("Texto dentro do arquivo") # Escreve o texto dentro do arquivo
#arquivo.close() # Fecha o arquivo
#arquivo = open("historico.txt", "r") # Abre o arquivo para leitura
#print(arquivo.read()) #Lê o texto dentro do arquivo e imprime
#arquivo.close() # Fecha o arquivo

