x = float(input("Digite o preço do produto1: "))
y = float(input("Digite o preço do produto2: "))
z = float(input("Digite o preço do produto3: "))

if x < y and x < z:
    print("O produto 1 é o mais barato então compre-o!!!")
elif y < x and y < z:
    print("O produto 2 é o mais barato então compre-o!!!")
elif z < x and z < y:
    print("O produto 3 é o mais barato então compre-o!!!")        