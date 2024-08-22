class Country:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.yuko = 0
        self.wazari = 0
        self.ippon = 0

    def add_points(self, points):
        self.points += points

    def add_yuko(self, yuko):
        self.yuko += yuko

    def add_wazari(self, wazari):
        self.wazari += wazari

    def add_ippon(self, ippon):
        self.ippon += ippon

def main():
    num_countries = int(input("Digite o número de países: "))
    countries = []

    for i in range(num_countries):
        country_name = input(f"Digite o nome do país {i+1}: ")
        country = Country(country_name)
        countries.append(country)

    rodadas = []
    while True:
        print("\nEscolha os confrontos da rodada:")
        for i, country in enumerate(countries):
            print(f"{i+1}. {country.name}")
        confrontos = []
        for i in range(num_countries // 2):
            country1_index = int(input(f"Digite o número do país 1 do confronto {i+1}: ")) - 1
            country2_index = int(input(f"Digite o número do país 2 do confronto {i+1}: ")) - 1
            confrontos.append((countries[country1_index], countries[country2_index]))
        rodadas.append(confrontos)

        print("\nRodada:")
        for country1, country2 in confrontos:
            print(f"{country1.name} x {country2.name}")
            result = input("Digite o resultado (V/E/D): ")
            if result.upper() == "V":
                country1.add_points(3)
                print(f"{country1.name} venceu!")
            elif result.upper() == "E":
                if input("Foi um empate em 0x0? (S/N): ").upper() == "N":
                    country1.add_points(1)
                    country2.add_points(1)
                print("Empate!")
            else:
                country2.add_points(3)
                print(f"{country2.name} venceu!")

            yuko1 = int(input(f"Quantos yuko {country1.name} fez? "))
            wazari1 = int(input(f"Quantos wazari {country1.name} fez? "))
            ippon1 = int(input(f"Quantos ippon {country1.name} fez? "))
            country1.add_yuko(yuko1)
            country1.add_wazari(wazari1)
            country1.add_ippon(ippon1)

            yuko2 = int(input(f"Quantos yuko {country2.name} fez? "))
            wazari2 = int(input(f"Quantos wazari {country2.name} fez? "))
            ippon2 = int(input(f"Quantos ippon {country2.name} fez? "))
            country2.add_yuko(yuko2)
            country2.add_wazari(wazari2)
            country2.add_ippon(ippon2)

        print("\nClassificação após a rodada:")
        countries.sort(key=lambda x: (x.points, x.ippon, x.wazari, x.yuko), reverse=True)
        for i, country in enumerate(countries):
            print(f"{i+1}. {country.name} - {country.points} pontos, {country.ippon} ippon, {country.wazari} wazari, {country.yuko} yuko")

        if len(rodadas) == num_countries - 1:
            break

    print("\nClassificação final:")
    countries.sort(key=lambda x: (x.points, x.ippon, x.wazari, x.yuko), reverse=True)
    for i, country in enumerate(countries):
        print(f"{i+1}. {country.name} - {country.points} pontos, {country.ippon} ippon, {country.wazari} wazari, {country.yuko} yuko")

if __name__ == "__main__":
    main()