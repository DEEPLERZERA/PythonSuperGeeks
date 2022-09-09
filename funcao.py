def resposta():  #Cria a função resposta
    resp = input('>: ')

    resp = resp.lower()

    resp = resp.replace('eh', 'é')
    resp = resp.replace('EH', 'é')
    return resp #Retorna a resposta



def pegaNome(nome): #Cria a função pegaNome
    if 'o meu nome é' in nome:
        nome = nome[13:]

    if 'O meu nome é' in nome:
        nome = nome[13:]
    return nome #Retorna o nome 

def respondeNome(nome):     #Cria a função respondeNome    

    conhecidos = ["natalia", "gustavo", "livia", "marcelo", "rauny", "kauan", "jessica", "daniel", "ricardo", "gleidson", "william", "andrey", "fabricio", "tutão", "marcio", "sifz", "joão", "ronoilson", "gaules"]

    if nome in conhecidos:
        frase = "Aoba pia! "

    else:
        frase = "Muito prazer "

    return frase + nome #Retorna a frase com o nome
