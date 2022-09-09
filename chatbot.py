from funcao import *

print("Olá qual é o seu nome?\n")

nome = pegaNome(resposta()) #Chama a função pegaNome e a função resposta
resp = respondeNome(nome) #Chama a função respondeNome e armazena na variável resp
print(resp) #Imprime a variável resp

while True:
  resp = resposta()
  if resp == "tchau":
        break
  else:
        print("Digite outra coisa.")



print("Bye Bye!")        


