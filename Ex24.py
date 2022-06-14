y = 0   #Declarando variável

for x in range(10):  #Para um range de 10 faça
    pessoa = int(input("Qual é a sua idade: "))  #Atribuindo idade das pessoas a variavel pessoa


    if pessoa >= 18:  #Fazendo verificação
        y += 1  #Aumentando número de y 


print("A quantidade de pessoas maiores de 18 anos é: ", y)   #Imorimindo dado na tela
    
