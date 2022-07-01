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







