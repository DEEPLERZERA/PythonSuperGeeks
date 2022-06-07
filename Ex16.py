temperatura = float(input("Digite uma temperatura em Celsius ou Farenheit: ")) 

conversao = input("Quer converter para qual temperatura Celsius ou Farenheit?: ").lower()

if conversao == "farenheit":
    F = (temperatura * 9/5) + 32
    print("Em Farenheit fica:" , F)
elif conversao == "celsius":
    C = (temperatura - 32) * 5/9
    print("Em Celsius fica:" , C)  

else:
    print("ERRO GRAVISSIMO DE LÓGICA!!!!!")      