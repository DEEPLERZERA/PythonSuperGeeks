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
    pass

valores = [7, 8, 3, 4, 2]  #Criando lista
print(valores) 
dobro(valores)
