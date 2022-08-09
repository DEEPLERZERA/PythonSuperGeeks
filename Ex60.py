def MaiorDeIdade():
    idade = input("Digite sua idade: ")
    if(int(idade) >= 18):
        print("Você é maior de idade!")
    elif(int(idade) < 0):
        print("Erro idade inválida")
    else:
        print("Você é menor de idade!")

MaiorDeIdade()                