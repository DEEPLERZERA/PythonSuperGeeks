import math  #Importando biblioteca math


fim = int(input("Digite um número ímpar: \n"))  #Recebendo input de valor final

inicio = 0  #Declarando que inicio é igual a 0

for x in range(math.ceil(fim/2)):  #Para um laço de repetição que recebe tais parametro faça
    for x in range(inicio, fim):  #Outro laço de repetição que parte do inicio e vai até fim
        print(x + 1, end = "")  #Imprime na tela valor de x mais 1 com o end = ""
    inicio += 1  #Aumenta valor de inicio
    fim -= 1  #Diminui valor de fim
    print("\n")  #Pula linha na tela