nome = "Daniel" #Declarando variáveis

idade = 17  #Atribuindo idade

print("Meu nome é", nome, "e eu tenho ", idade, "anos") #Imprimindo na tela
print("Meu nome é " + nome + " e eu tenho " , idade , "anos")  #Imprimindo na tela com + só que não aceita int


#Estilo C

print('Meu nome é %s e tenho %d anos.' % (nome, idade))   #Printando no estilo c -__-
print(
    'Meu nome é %(nome)s e tenho %(idade)d anos.' % {
        "nome":nome, "idade": idade}
    
)

#.format

print('Meu nome é {} e tenho {} anos.' .format(nome, idade))    #Pritando na tela com .format
print('Meu nome é {0} e tenho {1} anos e repito meu nome é {0}.' .format(nome, idade))
print('Meu nome é {nome} e tenho {idade} anos.' .format(nome = nome, idade = idade))


#f string

print(f'Meu nome é {nome} e tenho {idade} anos.')  #Um estilo muito bom para se printar na tela   
print(f'Um texto qualquer')


print('Ela disse "Bom dia".')  #Imprimindo com aspas dupla dentro

print("Caixa d'Agua")

print("Ela disse \"Bom dia\"")  #Imprimindo com caractere de escape