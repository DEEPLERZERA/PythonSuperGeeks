lista = []  #Cria lista

for x in range(5):  #Cria laço de repetição
    lista.append(int(input("Digite um valor de número inteiro: ")))  #Atribui valores a lista


if sorted(lista) == lista:  #Faz verificador se lista está em ordem crescente
    print("TRUE")  #Se sim imprime true

else:   #Se for false imprime
    print("FALSE")    #False





