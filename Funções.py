#Funções

print('Bom dia Daniel')
print('Bom dia Livia')
print('Bom dia Gustavo')
print('Bom dia Kauan')

def bomdia(nome):  #Cria função que recebe parâmetro
    print(f'Bom dia {nome}')  #Imprime na tela

bomdia('Marcio')    #Chama função passando parâmetro


#for x in range(10):  #Laço de repetição
   #bomdia('Daniel')


def soma(x, y):  #Criando função de somar
    z = x + y #Faz soma
    print(f'O valor de {x} + {y} é: {z}\n')  #Imprime na tela

soma(5, 5)    #Chama função de somar
soma(5, 15)    #Chama função de somar

soma(y=8, x=5) #Especificando variáveis e somando

#--------------------------------------------------------------------------------------------------------------
                                            #EMPACOTAMENTO

def contador(*num):  #Criamos uma função contador
    print(num) #Imprimindo na tela
    for numero in num: #Percorrendo tupla
        print(numero)

contador(5, 8, 6)  #Chamando função
contador(7, 8, 3, 4, 2)
contador(6, 4)


def dobro(lista):  #Criando função que faz dobro de lista
    pos = 0
    while pos < len(lista): #Percorre enquanto for menor que lista
        lista[pos] *= 2 #Duplica
        pos = pos + 1 #Aumenta posição para encerrar loop

valores = [7, 8, 3, 4, 2]  #Criando lista
print(valores, " antes de dobrar")  #Imprime na tela
dobro(valores)
print(valores, " depois de dobrar")

#Retorno

def sub(x, y): #Cria função de subtração
    z = x - y
    return z #Retorna z

z = sub(10, 5)  #Chama função de subtração e atribui a z

print(f"O resultado é {z}") #Imprime na tela


#PARAMETROS OPCIONAIS

def soma(x, y, z = 0):  #O terceiro parâmetro passa a ser opcional
    r = x + y + z
    print(r)

soma(1, 2)  #CHAMA FUNÇÃO


#VARIÁVEIS LOCAIS E GLOBAIS

def teste():  
    global b #Declaro que variável é global
    n = 5  #Variável local
    b = 8 #Este b é global 
    print(f"O valor de n de dentro é: {n}")

n = 2  #Variável local, agora se eu deletar o n de dentro e deixar só o de fora este passa a ser global

print(f"O valor de n de fora é: {n}")
teste()
print(f"O valor de n de fora é: {n}")
print(f"B é: {b}")










