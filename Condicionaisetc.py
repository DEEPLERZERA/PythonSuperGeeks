from re import X


numero = int(input("Digite um numero: \n"))  #Declarando a variavel

if numero > 0:  #Condicional
    print("O número é positivo!!!!") #Imprimindo na tela
elif numero == 0:  #Se não for verifique se numero == 0 
     print("O número é igual a zero!!!!")  #imprimindo na tela
else: #Se não faça
    print("O número não é positivo!!!!")  #Imprimindo na tela


#Mal exemplo

#if numero > 0:
    #print("Maior")

#if numero == 0:
    #print("Zero")

#if numero < 0:   
    #print("Menor")


#num1 = float(input("Digite um número: \n"))  #Criando variável e pedindo input float
#num2 = float(input("Digite um número: \n"))  #Criando variável e pedindo input float

#if num1 > 0 and num2 > 0:  #Criando condicional
 #print("Os dois numeros são positivos!!!15")   #Imprimindo na tela    
#else:  #Se não faça
 #print("Um deles não é positivo!!!")   #Imprima na tela



#if num1 == 10 or num2 == 20:  #Criando condicional e verificando se uma das expressoes é verdadeira
    #print("Um deles vale 10 ou 20!!!")  #Imprimindo na tela

#else:  #Se não faça
    #print("Nenhum deles vale 10 ou 20!!!")  #Imprima na tela mensagem


#if num1 > 10 and num1 <=20:  #Criando condicional onde ambas as expressões devem ser verdadeiras
    #print("Voce pode participar de um concurso!!!!")  #Caso verdade imprima na tela


nota = -1
while nota < 0 or nota > 10:  #Criando laço de repetição
    nota = int(input("Digite sua nota:  \n")) #Recebendo input
    if nota > 10:  #Condicional
        print("Nota maior que 10!!!")  #Imprimindo
    elif nota < 0:   #Condicional
        print("Nota menor que zero?")
    else:
        print("Errado apenas...")        
if nota>= 9: #Criando condicional
    print("Parabens voce passou")  #Imprimindo na tela
elif nota >=7:  #Se não faça
    print("Parabens passou apertado") #Imprime na tela
elif nota >=5: #Se  não faça
    print("Ficou de recuperacao!!!") #Imprime na tela
else: #Se não faça
    print("Reprovado!!!!") #Imprime na tela 










    



