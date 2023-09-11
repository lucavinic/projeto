import requests
from bs4 import BeautifulSoup
def get_best_odds(jogo, mais_de_menos):
  """
  Obtenha as melhores odds para um determinado jogo e mais/menos.
  Args:
    jogo: O jogo para apostar.
    mais_de_menos: O mais/menos para o jogo.
  Returns:
    Uma lista de tuplas contendo as odds e a casa de apostas para cada uma das melhores odds.
  """
  # Obtenha o HTML para o jogo.
  url = "https://www.oddschecker.com/futebol/campeonato-ingles/jogo/liverpool-x-manchester-city/vencedor"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  # Encontre as odds para o jogo.
  odds_table = soup.find("table", {"class": "oddsTable"})
  if odds_table is None:
    return []
  odds_rows = odds_table.find_all("tr")
  # Encontre as melhores odds para o jogo.
  best_odds = []
  for row in odds_rows:
    odds_cells = row.find_all("td")
    if odds_cells[0].text == jogo and odds_cells[1].text == mais_de_menos:
      best_odds.append((float(odds_cells[2].text), odds_cells[3].text))
  # Retorne as melhores odds.
  return best_odds
# Obtenha as melhores odds para o jogo.
best_odds = get_best_odds("Liverpool x Manchester City", "Mais de 2,5 gols")
# Imprima as melhores odds.
for odds, sportsbook in best_odds:
  print(f"{sportsbook}: {odds}")