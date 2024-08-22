class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0

    def adiciona_resultado(self, resultado, pontos):
        if resultado == 'V':
            self.vitorias += 1
            self.pontos += pontos
        elif resultado == 'E':
            self.empates += 1
            self.pontos += pontos
        elif resultado == 'D':
            self.derrotas += 1

def classifica_equipes(equipes):
    equipes.sort(key=lambda x: (x.pontos, x.vitorias, x.empates), reverse=True)
    return equipes

def main():
    num_equipes = int(input("Digite o número de equipes no grupo: "))
    equipes = []
    for i in range(num_equipes):
        nome_equipe = input(f"Digite o nome da equipe {i+1}: ")
        equipes.append(Equipe(nome_equipe))

    num_lutas = int(input("Digite o número de lutas que cada equipe irá disputar: "))

    for i in range(num_lutas):
        for equipe in equipes:
            resultado = input(f"Digite o resultado da luta {i+1} da equipe {equipe.nome} (V, E ou D): ")
            pontos = int(input(f"Digite os pontos da luta {i+1} da equipe {equipe.nome}: "))
            equipe.adiciona_resultado(resultado, pontos)

    equipes_classificadas = classifica_equipes(equipes)

    print("\nClassificação final:")
    for i, equipe in enumerate(equipes_classificadas):
        print(f"{i+1}. {equipe.nome} - {equipe.pontos} pontos, {equipe.vitorias} vitórias, {equipe.empates} empates e {equipe.derrotas} derrotas")

    num_equipes_classificadas = int(input("Digite o número de equipes que se classificam para a próxima fase: "))

    for i in range(num_equipes_classificadas):
        print(f"A equipe {equipes_classificadas[i].nome} se classificou para a próxima fase!")

if __name__ == "__main__":
    main()