soma = 0   #Declara variáveis
soma2 = 0
n = int(input("Digite um número: "))  #Pega input
if soma > n:
    while soma > n:  #Cria laço de repetição
        n += 1  #Cria incremento
        soma2 = soma2 + n #Faz soma
    print(soma2)  #Imprime na tela
else:    

    while soma < n:  #Cria laço de repetição
        soma += 1  #Cria incremento
        soma2 = soma2 + soma #Faz soma
    print(soma2)  #Imprime na tela
    
   
    


