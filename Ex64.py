def primo():
    n = int(input("Verificar números primos até: "))
    mult = 0

    for x in range(2, n):
        if(n % x == 0):
            print(f"Múltiplo de {x}")
            mult += 1

    if(mult == 0):
        print("É primo!")
    else:
        print(f"Tem {mult} múltiplos acima de 2 e abaixo de {n}")    

primo()        