soma = 0 #Declarando variáveis
soma2 = 0
n = int(input("Digite um número: "))  #Pega input

if n >= 10:  #Faz verificação
    while soma < n:  #Cria laço de repetição
        soma += 1  #Faz incremento
        if soma % 2 == 0: #Faz condicional
            soma2 = soma2 + soma  #Cria soma
    print(soma2)  #Imprime valor na tela
else:  #Se não faça
    print("Valor não é menor igual a 10!!!!") #Imprime na tela   