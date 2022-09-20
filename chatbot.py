from bot import Bot # Importa a classe Bot

bot = Bot("Andrew") # Cria o objeto bot


while True:
  frase = bot.escuta() # Escuta a frase
  resp = bot.pensa(frase) # Pensa na resposta
  bot.fala(resp) # Fala a resposta

  if frase == "tchau": # Se a frase for tchau
        break # Para o loop



print("Bye Bye!")  # Imprime a mensagem de despedida     















#print(eval("1+1")) # Imprime 2
#a = 10

#try:     # Tenta executar o código
  #print(a) # Imprime a variável a
  #print(1/0) # Imprime a variável b
  #open('jasdasdasdasadaf', 'r') # Abre um arquivo json
#except NameError: # Se der erro
  #print("A variável 'a' não existe!")  # Imprime a mensagem de erro


#except (FileNotFoundError, ZeroDivisionError): # Se der erro
  #print("Arquivo não encontrado ou você está tentando dividir por zero!") # Imprime a mensagem de erro


#finally:
  #print("O programa terminou!") # Imprime a mensagem de erro


#arquivo = open("historico.txt", "w") # Abre o arquivo para escrita
#arquivo.write("Texto dentro do arquivo") # Escreve o texto dentro do arquivo
#arquivo.close() # Fecha o arquivo
#arquivo = open("historico.txt", "r") # Abre o arquivo para leitura
#print(arquivo.read()) #Lê o texto dentro do arquivo e imprime
#arquivo.close() # Fecha o arquivo

