import random   #Importando a biblioteca

x = random.randint(0, 10)  #Randomizando números
n = -50  #Atribuindo variável
y = 0
while n != x: #Faça enquanto
    n = int(input("Tente adivinhar o número: "))  #Receba input
    y += 1  #Faça incremento
print("Parabéns você descobriu o número!!!! " , x)  #Imprima na tela
print("Você fez ", y, "Tentativas!")  #Imprima na tela
