soma = 0  #Declaração de variáveis
x = 0
y = 0
digitados = 0

while digitados < 2: #Criando laço de repetição
    x = int(input("Digite o primeiro número: "))  #Recebendo inputs
    y = int(input("Digite o segundo número: "))
    soma = x + y  #Fazendo soma
    print("A soma da ", soma)   #Imprimindo na tela
    opcao = input("Deseja continuar o programa tecle Y/N: ")  #Recebe input

   
    if opcao == "Y":  #Condicional
        digitados = 0  #Atribui valor a variável
    else:   #Se não faça
        print("Fim do programa")  #Imprime na tela
        break     #Quebra laço de repetição
