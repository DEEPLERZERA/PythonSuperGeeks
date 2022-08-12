def fatorial():

    n = int(input("Digite o valor que quer calcular o fatorial: "))

    fat = 1  
    i   = 2

    while i <= n:
        fat = fat * i 
        i += 1 
    print(f"O valor de {n} fat é = {fat}")

fatorial()        