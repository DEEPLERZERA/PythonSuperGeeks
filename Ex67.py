class conta_corrente:
    def __init__(self, nome, banco, conta, saldo):
        self.nome = nome 
        self.banco = banco 
        self.conta = conta 
        self.saldo = saldo 



    def saque(self):
        if self.saldo > 0:
            print("Você pode realizar saques!")
            valor = input("Quanto deseja retirar?: ")
            self.saldo = self.saldo - int(valor)
            print(f"Agora você tem {self.saldo} reais na sua conta!")  
        if self.saldo <= 0:
            print("Não pode fazer mais realizar saques, pois seu dinheiro é insuficiente!")    

    def deposito(self):
        valor = input("Quanto deseja colocar?: ")
        self.saldo = self.saldo + int(valor)
        print(f"Agora você tem {self.saldo} reais na sua conta!")  

    def consultar_saldo(self):
        self.saldo = self.saldo
        print(f"Você tem {self.saldo} reais na sua conta!")

    def pix(self):
        if self.saldo > 0:
            print("Você pode realizar transferências pix!")
            pix = input("Digite o pix do favorecido: ")
            valor = input("Quanto deseja transferir?: ")
            self.saldo = self.saldo - int(valor)
            print(f"O valor de {valor} reais foi para o pix {pix}")
            print(f"Agora você tem {self.saldo} reais na sua conta!")  
        if self.saldo <= 0:
            print("Não pode fazer mais realizar transferências pix, pois seu dinheiro é insuficiente!") 
p1 = conta_corrente("daniel", "bradesco", 239393, 5000)
p1.saque()
p1.deposito()
p1.consultar_saldo()
p1.pix()


