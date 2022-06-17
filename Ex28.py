alto = 0   #Atribuindo valor


for x in range(5):  #Criando laço de repetição
    y = int(input("Digite um valor inteiro: "))   #Entrando com input do usuário
    if(y > alto):  #Laço de verificação
        alto = y   #Se for atendido a condição atribui y a alto

print("O maior valor é: ", alto)    #Imprimindo na tela      

        