#Matriz

alunos = ["Ana", "João", "Maria"] #Cria array

alunos2  = ("Daniel", "Paula", "Pedro") #Cria array tupla 

alunos3 = [  #Cria array multidimensional
    ["Daniel", "Jéssica", "Kauan", "Ricardo", "Gustavo", "Livia"],
    [18,          14,       16,       10,         17,       14],
    ["BH",       "RJ",     "SP",     "BA",        "PA",   "SP"],
    [1.75,       1.60,     1.72,     1.80,        1.82,   1.65],
    ]

print(alunos3[2])    #Imprime vetor na tela

print(alunos3[0][1]) #Imprime na tela de acordo com vetores


nome = ["Daniel"]  #Criando variáveis

sexo = ["m"]

telefone = ["11956281384"]

cadastro = [] #Criando lista

cadastro.extend([nome, sexo, telefone])  #Adicionando itens a lista

print(cadastro)

nome[0] = "Gustavo"  #Alterando variáveis

sexo[0] = "m"

telefone[0] = "9876543321"

print(nome)

print(cadastro)

cadastro.extend([nome, sexo, telefone])  #Repetindo dados na lista

print(cadastro) 

nome[0] = "Daniel" #Mudando variável nome novamente

print(cadastro)


nomeNovo = []  #Criando arrays
nomeAntigo = []

nomeAntigo.insert(0, cadastro[0][0])  #Adicionando cadastro[0][0] ao nomeAntigo

nomeNovo.append(cadastro[0])  #Adicionando cadastro[0] a nomeNovo

nome[0] = "Kauan"  #Alterando variáveis

print(f"Nome novo: {nomeNovo}")  #Imprimindo na tela resultados
print(f"Nome antigo: {nomeAntigo}")
print(f"Cadastro: {cadastro}")


telefone.clear()  #Apagando telefone
print(cadastro)



nome2 = cadastro[0]

print(nome)
print(nome2)
print(nomeNovo)
print(nomeAntigo)


print(id(nome))  #Imprime id das variáveis
print(id(nome2))

print(id(nomeAntigo))
print(id(nomeNovo))









