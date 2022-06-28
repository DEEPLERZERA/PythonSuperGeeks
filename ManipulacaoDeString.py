#Manipulação de String

nome = "rauny"

idade = 17

#Método title: Deixa a primeira letra maiúscula

print(nome)  #Sem a função imprime minusculo
print(nome.title())  #Com title imprime primeira letra maiuscula
nome2 = nome.title() #Atribui nome com primeira letra maiuscula na variavel nome2
print(nome2)  #Imprime minusculo

#Método len

pets = ["Gato", "Cachorro", "Peixe"] #Criando array  

print(len(pets)) #Imprime a quantidade de itens da array

print(len(nome)) #Imprime numero de caracteres numa string

print(f'Eu sou o {nome.title()}.\n'    #Fazendo uma série de prints
    f'Em 2023 eu vou fazer {idade + 1} anos.\n'
    f'Tenho {len(pets)} animais de estimação.'
)


#método type

print(type(nome))  #Imprimindo tipos da variável
print(type(idade))

idadeStr = str(idade) #Transformando idade em string
print(type(idadeStr))  #Imprimindo tipo

#Método replace

frase = "Meu nome é Marcelo!" #Declarando variável

print(frase)  #Imprimindo
print(frase.replace("Marcelo", "Ricardo"))  #Trocando Marcelo por Ricardo

#Método startswith

print(frase.startswith("Meu"))  #Retorna booleano e verifica se a frase  passada começa com o parâmetro dado
print(frase.startswith("meu"))
print(frase.startswith("nome", 4, 8)) #Verifica de acordo com o intervalo passado e retorna booleano

print(frase.startswith("nome", 4, 6)) 

#Método endswith

print(frase.endswith("Marcelo!")) #Verifica se encerra com o parâmetro passado
print(frase.endswith("sugoi"))
print(frase.endswith("nome",0, 4))  #Verifica dentro do intervalo

#Método count

print(frase.count("e")) #Verifica quantos "e" tem em nossa frase!







