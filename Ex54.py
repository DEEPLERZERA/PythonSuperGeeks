def idade():
    nas = input("Digite o ano que nasceu: ")
    atual =  input("Digite o ano atual: ")
    idade = int(atual) - int(nas)
    print(f"Você têm: {idade}") 

idade()