class mamifero:
    def __init__(self, especie, genero, n_patas):
        self.genero = genero 
        self.n_patas = n_patas
        self.especie = especie

    def falar(self):
        print(f"O {self.especie} Mamifero está falando...")


    def andar(self):
     print(f"O {self.especie} Mamifero está andando...")

    def amamentar(self):
        if self.genero == 'macho':
            print(f"{self.especie} Mamifero macho não pode amamentar")
            return
        print(f"{self.especie} Mamifero está amamentando...")         

class cachorro(mamifero):
    def __init__(self, especie, genero, n_patas, cor_pelo):
        super().__init__(especie, genero, n_patas)
        self.cor_pelo = cor_pelo

class humano(mamifero):
    def __init__(self,especie, genero, n_patas, cabelo):
        super().__init__(especie, genero, n_patas)
        self.cabelo = cabelo 

c1 = cachorro("Cachorro",'macho', 4, "branco")
c1.falar()
c1.amamentar()
h1 = humano("Humano",'femea', 2, "castanho")
h1.falar()
h1.amamentar()
h1.andar()

