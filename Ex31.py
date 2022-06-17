qtd = 0 #Atribui valor a variável

for x in range(10):  #Cria laço de repetição
    y = int(input("Digite um número inteiro: "))  #Atribui valor a variável y pegando input do usuário
    if  y > 0 and y <= 50:  #Faz verificador
       qtd += 1 #Incrementa

print("São ", qtd, "De 0 a 50!!!")         #Imprime na tela
