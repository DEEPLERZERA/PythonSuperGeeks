x = float(input("Digite um numero: "))
y = float(input("Digite um outro numero: "))

operacao = int(input("Qual operação tu desejas fazer? para multiplicacao digite 1 e para divisao digite 2: "))

if operacao == 1:
    resultado = x * y
    print("Resultado é:" , resultado)
elif operacao == 2:
    resultado = x / y
    print("Resultado é:" , resultado)    

else:
    print("Operacao invalida!!!!!")


