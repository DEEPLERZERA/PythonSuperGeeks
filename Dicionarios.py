#Dicionarios

from ast import alias


lista = ['ana', 5, 1.8]

tupla = ('ana', 5, 1.8)

matrizTeste = (('ana', 5, 1.8),
                ['ana', 5, 1.8])


aluno = {'nome' : ['Natalia'], 'idade' : 47, 'estado' : 'SP'}  #Criando dicionario


print(aluno['nome'])
print(aluno['idade'])
print(aluno['estado'])

print(aluno.keys())  #Imprime os campos
print(aluno.values()) #Imprime os valores dos campos
print(aluno.items()) #Imprime tudo

for x in aluno.keys():  #Vai percorrendo e imprimindo
    print(x)

for x in aluno.values():
    print(x)

for x, y in aluno.items():
    print(f'A chave {x} possui o valor: {y}.')


print(len(aluno)) #Imprime tamanho

aluno['nome'] = "joão"  #Alteramos os dados
print(aluno)

aluno['altura'] = 1.65  #Adicionamos novo campo e dado
print(aluno)

#aluno['nome'].append('Clara')

print(aluno)
       

alunos = {'nome': ["ana", "joão"], 'idade': [17, 16], 'estado' : ["SP", "RJ"]}  #Criando lista

print(alunos)

print(alunos['nome'][1]) #Mostra dado específico

alunos['nome'].append('jose') #Adiciona dado no campo
print(alunos)

alunos['altura'] = 1.81  #Novo campo e dado

print(alunos)
alunos.pop('altura')  #Remove campo
print(alunos.pop('altura', "Não tem está chave!"))  #Se não tiver mais o campo imprime mensagem de erro
print(alunos)


#dados = ["nome", "idade", "altura"]  #Cria lista de dados

#cadastro = {}  #Dicionário

#for x in dados:  #Loop for
    #cadastro[x] = str(input(f'Digite a informação do {x}: ')) #Vai atribuindo a cadastro


#print(cadastro)

estado = dict()  #Cria dicionário vazio
brasil = list() #Cria lista vazia


for x in range(3):  #Loop for
    estado['uf'] = str(input("Digite o nome do estado: "))  #Recebe dados
    estado['sigla'] = str(input("Digite a sigla do estado: "))
    brasil.append(estado.copy())  #Vai atribuindo a lista

print(brasil)    


print(brasil[0]['sigla'])    #Acessa dado específico



