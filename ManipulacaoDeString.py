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


#Método count

print(len(frase))  #Imprime na tela quantidade de caracteres
print(frase.count("M"))  #Imprime quantidade desta letra


#Método Capitalize

frase =  "mEu NoMe É JoÃo."  #Criando variável

print(frase.title())  #Deixa o inicio de cada nome em letra maiúscula
print(frase.capitalize())   #Deixa só a primeira letra Maiúscula

#Método isdigit

telefone = "36918285" #Criando variável

nome = "Lívia"

Palavra = "amora123"

print(telefone.isdigit())  #Verifica se é tudo número e retorna boolean

print(nome.isdigit())

print(Palavra.isdigit())

print(nome.isalpha()) #Verifica se é tudo letra e retorna boolean


print(Palavra.isalnum()) #Verifica se é letra ou número e retorna boolean


#Método upper e lower

aluno = "kauan"
aluno2 = "jEssIca"


print(aluno.upper()) #Transforma tudo em maiúsculo
print(aluno2.lower()) #Retorna tudo minúsculo


#Método find

Nome = "Daniel"  #Criando variáveis

print(Nome.find("a")) #Retorna em qual índice a palavra está


#Método split

nome3 = "Andrey Ferreira Pichuti"  #Criando variável

listanome = nome3.split()  #Recorta a variável inteira e guarda nesta listanome

print(listanome) #Imprime na tela


listanome2 = nome3.split("r")  #Define a onde você quer que ele corte a string
print(listanome2) #Imprime na tela


#Método join

nome3 = "William Cellegin Utsunomiya Dos Santos"  #Cria variável

separado =  nome3.split()  #Corta string 

print(separado) #Imprime na tela

print("-_-".join(separado)) #Une a variável que está com tudo quebrado de novo


#Método strip 

nome4 = "                           Carlos Alberto de Nobrega" #Cria variáveis
nome5 = "                                                    Carlos Andrade Da Costa"

print(nome4.strip()) #Tira os espaços e imprime na tela
print(nome5.strip()) #Tira os espaços e imprime na tela
















