y = 0   #Declarando variável
pessoas = 0 #Declarando a variável

for x in range(7):  #Para um range de 10 faça
    pessoa = int(input("Qual é a sua idade: "))  #Atribuindo idade das pessoas a variavel pessoa
    peso = int(input("Qual é o seu peso: ")) #Atribuindo peso das pessoas a variavel peso
    pessoas += pessoa  #Somando quantidade de idades para no final calcular a média

    if peso > 90:  #Fazendo verificação
        y += 1  #Aumentando número de y 


media = pessoas/7  #Calculando media da idade das pessoas

print("A quantidade de pessoas com mais de 90 quilos é: ", y)   #Imorimindo dado na tela
print("A média de idade das pessoas é: ", media)  #Imprimindo média de pessoas
    