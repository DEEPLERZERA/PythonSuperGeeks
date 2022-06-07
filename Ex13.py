dia = int(input("Digite o dia do seu aniversário: "))
mes = int(input("Digite o mês do seu aniversário: "))
ano = int(input("Digite o ano do seu aniversário: "))

if dia > 31 or dia < 1:
    print("Erro dia inexistente no calendario atual!!!!")
if mes < 1 or mes > 12:
    print("Erro mês inexistente no calendario atual!!!!")
if ano < 1850 or ano > 2022:
    print("Ano de aniversário invalido!!!")        

else:
    print("Seu aniversário ocorre na data de: " , dia , "/" , mes , "/" , ano)    