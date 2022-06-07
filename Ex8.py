x = float(input("Digite um número: "))
y = float(input("Digite um segundo número: "))
z = float(input("Digite um terceiro número: "))

if x > y and x > z:
    print("numero 1 é maior que todos!!!")
elif y > x and y > z:
    print("numero 2 é maior que todos!!!!") 

elif z > x and z > y:
    print("numero 3 é maior que todos!!!!")

elif x == y and x == z:
    print("Todos os elementos são iguais")


