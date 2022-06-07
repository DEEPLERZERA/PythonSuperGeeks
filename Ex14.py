irmao = input("Voce tem irmãos?: ").lower()

if irmao == "sim":
    quantos = input("Quantos irmãos você tem?: ")
    print("Então você tem:" , quantos, "irmãos!!!")

elif irmao == "não":
    gostaria = input("Gostaria de ter?: ")
    print("Então você " , gostaria, " Gostaria de ter um irmão!!!!") 

else:
    print("Opção invalida!!!")      