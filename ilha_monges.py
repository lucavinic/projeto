class Estado:
    def __init__(self, monges_esquerda, canibais_esquerda, monges_direita, canibais_direita, barco):
        self.monges_esquerda = monges_esquerda
        self.canibais_esquerda = canibais_esquerda
        self.monges_direita = monges_direita
        self.canibais_direita = canibais_direita
        self.barco = barco

    def __str__(self):
        return f"Monges Esquerda: {self.monges_esquerda}, Canibais Esquerda: {self.canibais_esquerda}, Monges Direita: {self.monges_direita}, Canibais Direita: {self.canibais_direita}, Barco: {self.barco}"

class Jogo:
    def __init__(self):
        self.estado_atual = Estado(3, 3, 0, 0, "esquerda")

    def ir(self, personagem1, personagem2):
        if self.estado_atual.barco == "esquerda":
            if personagem1 == "monge":
                self.estado_atual.monges_esquerda -= 1
                self.estado_atual.monges_direita += 1
            else:
                self.estado_atual.canibais_esquerda -= 1
                self.estado_atual.canibais_direita += 1
            if personagem2 == "monge":
                self.estado_atual.monges_esquerda -= 1
                self.estado_atual.monges_direita += 1
            else:
                self.estado_atual.canibais_esquerda -= 1
                self.estado_atual.canibais_direita += 1
            self.estado_atual.barco = "direita"
        else:
            print("Erro: o barco já está do outro lado.")

    def voltar(self, personagem):
        if self.estado_atual.barco == "direita":
            if personagem == "monge":
                self.estado_atual.monges_direita -= 1
                self.estado_atual.monges_esquerda += 1
            else:
                self.estado_atual.canibais_direita -= 1
                self.estado_atual.canibais_esquerda += 1
            self.estado_atual.barco = "esquerda"
        else:
            print("Erro: o barco já está deste lado.")

    def verificar_regras(self):
        if self.estado_atual.monges_esquerda < self.estado_atual.canibais_esquerda and self.estado_atual.monges_esquerda != 0:
            return False
        if self.estado_atual.monges_direita < self.estado_atual.canibais_direita and self.estado_atual.monges_direita != 0:
            return False
        return True

    def jogar(self):
        while True:
            print(self.estado_atual)
            acao = input("Digite 'ir' para ir com dois personagens ou 'voltar' para voltar com um personagem: ")
            if acao == "ir":
                personagem1 = input("Digite o primeiro personagem (monge ou canibal): ")
                personagem2 = input("Digite o segundo personagem (monge ou canibal): ")
                self.ir(personagem1, personagem2)
            elif acao == "voltar":
                personagem = input("Digite o personagem que deseja voltar (monge ou canibal): ")
                self.voltar(personagem)
            else:
                print("Erro: ação inválida.")
                continue
            if not self.verificar_regras():
                print("Erro: regras do jogo violadas. Game over.")
                break
            if self.estado_atual.canibais_direita == 3:
                print("Parabéns, você venceu!")
                break

jogo = Jogo()
jogo.jogar()