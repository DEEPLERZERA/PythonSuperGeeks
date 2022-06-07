per1 = input("Telefonou para a vitima?: ")
per2 = input("Esteve no local do crime?: ")
per3 = input("Mora perto da vítima?: ")
per4 = input("Devia para a vítima?: ")
per5 = input("Trabalhou com a vítima: ")
teste = 0

if per1 == "sim":
    teste += 1
if per2 == "sim":
    teste += 1
if per3 == "sim":
    teste += 1
if per4 == "sim":
    teste += 1 
if per5 == "sim":
    teste += 1   

if teste < 2:
    print("Inocente")
elif teste == 2:
    print("Suspeita") 
elif teste <= 4:
    print("Cúmplice")
elif teste == 5:
    print("Assasino")                 

