def MenorValor():
    x = input("Digite um valor: ")
    y = input("Digite um segundo valor: ")
    if(x < y):
        print(f"{x} é o menor!")
    elif(x == y):
        print("Erro valores iguais!")    
    else:
        print(f"{y} é o menor!")



MenorValor()            