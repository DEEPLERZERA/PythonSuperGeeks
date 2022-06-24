import random  #Importando bibliotecas

vitoriaspc = 0  #Declarando variáveis
vitoriasuser = 0

n = 0
while n <= 3:  #Criando laço de repetição
    computador = random.randint(0, 2)  #Randomizando escolhas do pc
    print("[0]Papel, [1]Pedra, [2]Tesoura")  #Imprimindo na tela
    usuario = int(input("Escolha sua opção: "))  #Pegando input do usuário
    if computador == 0: #Criando laço de repetição
        print("O computador escolheu Papel!")  #Imprimindo na tela
        if usuario == 0:
            print("Empate!")
        elif usuario == 1:
            print("Perdeu!")
            vitoriaspc += 1
        elif usuario == 2:
            print("Ganhou!")
            vitoriasuser += 1
    elif computador == 1:
        print("O computador escolheu Pedra!")
        if usuario == 0:
            print("Ganhou!")
            vitoriasuser += 1
        elif usuario == 1:
            print("Empate!")
        elif usuario == 2:
            print("Perdeu!")
            vitoriaspc += 1
    elif computador == 2:
        print("O computador escolheu Tesoura!")
        if usuario == 0:
            print("Perdeu!")
            vitoriaspc += 1
        elif usuario == 1:
            print("Ganhou!")
            vitoriasuser += 1
        elif usuario == 2:
            print("Empate!")
    n += 1    #Fazendo incremento      


if vitoriaspc > vitoriasuser:   #Criando laço verificador
    print("O pc venceu com ", vitoriaspc, "Vitórias!")  #Imprimindo na tela
elif vitoriaspc == vitoriasuser:  #Se não faça 
    print("Empate geral entre pc e usuário")  #Imprima na tela
else:   #Se não faça
    print("O usuário venceu com ", vitoriasuser, "Vitórias!")   #Imprima na tela
