print("Olá qual é o seu nome?\n")
nome = input('>: ')

nome = nome.lower()

if 'o meu nome é' in nome:
    nome = nome[13:]
    
conhecidos = ["natalia", "gustavo", "livia", "Marcelo", "Rauny", "Kauan", "Jessica", "Daniel", "Ricardo", "Gleidson", "William", "Andrey", "Fabricio", "Tutão", "Marcio", "Sifz", "João", "Ronoilson", "Gaules"]

if nome in conhecidos:
    frase = "Aoba pia! "

else:
    frase = "Muito prazer "

print(frase + nome)


while True:
    resposta = input('>: ')
    if resposta == "tchau":
        break
    else:
        print("Digite outra coisa.")



print("Bye Bye!")        


