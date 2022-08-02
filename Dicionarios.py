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
print(alunos)