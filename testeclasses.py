
class Cachorros:
    def __init__(self):
        self.nome = None
        self.raca = None
        self.comprimento = None
        self.peso = None
        self.cadastro()
        self.acao()

    def cadastro(self):
        self.nome = input("Qual o nome do seu pet? ").capitalize()
        self.raca = input("Qual a raça dele? ").capitalize()
        self.comprimento = float(input("Qual o comprimento do seu pet? "))
        self.peso = float(input("Qual o peso dele? "))

    def acao(self):
        print(f"Meu nome é {self.nome}. AU AU AU!")
        print(f"Minha raça é {self.raca}!")
        print(f"Tenho {self.comprimento:.2f}cm de comprimento!")
        print(f"Peso {self.peso:.2f}Kg")

acoes = Cachorros()

