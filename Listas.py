#LISTA

lista1 = ["a", "B", "G",1, 8, 10.1, "t", True] #Criando uma array

print(lista1) #Imprime toda a lista

print(lista1[2]) #Imprime G

print(lista1[5]) #Imprime 10.1

for x in lista1:  #Percorre a array
    print(x)  #Vai imprimindo na tela

for x in range(len(lista1)):  #Percorre a array de acordo com número da array
    print(f"{x} Elemento da lista: {lista1[x]}")    #Imprime na tela número da array e valor de acordo com índice



#Método index

print(lista1.index("t")) #Imprime índice do parâmetro passado


#Somandos listas

a = ["A", "B", "C"] #Criando arrays
b = ["D", "E", "F"]

ab = a + b #Somando arrays

print(ab)  #Imprimindo na tela


#Método append

bbb = ["Daniel", "Andrey", "William", "Fablab", "Sifz", "Mazé", "Dudu", "TUTAO"] #Cria array
print(bbb)  #Imprime na tela
bbb.append("João") #Adiciona João no array
print(bbb) #Imprime na tela


#Método extend

bbb.extend(["Maaarcio", "Nilzaaa"])  #Adiciona mais itens na array de uma vez
print(bbb) #Imprime na tela


#Método insert

bbb.insert(0,"Rauny") #Define em que posição entra no array

print(bbb) #Imprime na tela

#Método remove: 

bbb.remove("William")  #Remove algum item da lista
print(bbb)  #Imprime na tela o array


#Método pop

bbb.insert(0, "Natalia")  #Adiciona elemento no array
print(bbb) #Imprime na tela
bbb.pop(1) #Remove índice 1 do array
bbb.pop(6) #Remove índice 6 do array
print(bbb)  #Imprime na tela


#Método clear

bbb.clear()  #Limpa array
print(bbb) #Imprime array na tela



#Método sorted

caracteres = ['X', 'B', '7', 'a', 'Q', '!', 'j', '5', '2']  #Criando array
print(sorted(caracteres)) #Deixa na ordem
print(caracteres)  #Imprime array completa

#Método min e max

numeros = ["6", "8", "1", "9", "4"] #Criando array

print(min(numeros)) #Descobre valor min
print(max(numeros)) #Descobre valor max


#tuplas

lista = [4, 2, 8, 6]  #Criando lista e tupla
tupla = (4, 2, 8, 6)  #Tupla não pode alterar o conteúdo

print(type(lista)) #Imprimindo tipos
print(type(tupla))


lista[0] = 5 #Mudando valor de índice 0
print(lista) #Imprimindo array


#Método sum

print(sum(tupla)) #Retorna soma da array


#Método sorted mais reverse

print(sorted(tupla)) #Imprime tupla em ordem crescente

print(tupla) #Imprime tupla 

print(sorted(tupla, reverse = True)) #Coloca tupla em ordem decrescente



#Método Sort

lista.sort()  #Deixa lista em ordem crescente definitivamente
print(lista)  #Imprime lista

lista.sort(reverse = True)  #Deixa a lista em ordem decrescente definitivamente

print(lista) #Imprime lista









