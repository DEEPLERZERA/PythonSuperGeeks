numero = 0  #Declarando a variável
digitados = 0  #Declarano a variável
soma = 0  
while numero != 999:  #Criando laço de repetição 
    numero = int(input("Digite um número: "))  #Recebendo input

    if numero == 999:  #Criando condicional
        digitados += 1  #Fazendo incremento
        soma = soma + numero  #Fazendo soma
        break  #Quebrando o laço de repetição
    else:  #Se não faça
        digitados += 1  #Incremento
        soma = soma + numero  #Soma
print("Você digitou ", digitados, "E a soma da ", soma)    #Imprima na tela      
        