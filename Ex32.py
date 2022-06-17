idademtotal = 0  #Atribuindo variáveis
idadehtotal = 0


for x in range(10):  #Criando laço de repetição
    sexo = input("Digite o seu sexo 'M' ou 'H': ")  #Recebendo input do usuário com relação ao seu sexo
    if sexo == "M":  #Criando Verificação
        idadem = int(input("Digite sua idade: ")) #Recebendo input
        idademtotal = idademtotal + idadem  #Fazendo soma
    elif sexo == "H":  #Caso não seja verdade faça
        idadeh = int(input("Digite sua idade: ")) #Recebe input
        idadehtotal = idadehtotal + idadeh #Fazendo soma
    else:
        print("Gênero invalido!")  #Gênero invalido

idademediam = idademtotal/10  #Fazendo calculos
idademediah = idadehtotal/10
idadegrupototal = idademtotal + idadehtotal
idademediagrupo = idadegrupototal/10

print("Idade média das mulheres é: ", idademediam)   #Imprimindo resultados
print("Idade média dos homens é: ", idademediah)
print("Idade média do grupo: ", idademediagrupo)

