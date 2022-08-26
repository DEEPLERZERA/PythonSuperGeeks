class A:  #Cria classe
    vc = 123
    def __init__(self, classe):
        self.classe = classe 

  
a1 = A("a1")  #Atriuindo dados
a2 = A("a2")

#A.vc = 321

a1.vc = 3214  #Altero valor de a1.vc

print(a1.__dict__)  #Imprime dicionario
print(a2.__dict__)
print(A.__dict__)

print(a1.vc)  #Imprime dados
print(a2.vc)
print(A.vc)