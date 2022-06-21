senha = ""  #Atribuindo variável

while senha != "123456":  #Criando laço de repetição 
    senha = input("Digite uma senha: ")  #Pedindo para inputar senha
    if senha != "123456":  #Condicional
        print("Senha incorreta tente novamente!!!")   #Imprimindo na tela
print("Seja bem-vindo!!!!")  #Imprimindo na tela      