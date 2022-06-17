u_1 = 0  #Atribuindo valores as variáveis
u_2 = 1
count = 0



for vic in range(0, 100):  #Criando laço de repetição
    count = u_1 + u_2  #Fazendo contador
    u_1 = count   
    u_2 = (count - u_2)
    print(count)  #Imprimindo na tela a cada passo do loop
    

