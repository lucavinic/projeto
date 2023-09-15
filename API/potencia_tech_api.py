import requests as r
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
resp.status_code
raw_data = resp.json()
raw_data[0]
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])
final_data
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
import datetime as dt
print(dt.time(12, 6, 21, 7)), ('Hora:minuto:segundo.microsegundo')
print('----')
print(dt.date(2020, 4, 25)), ('Ano-mês-dia')
print('----')
print(dt.datetime(2020, 4, 25, 12, 6, 21, 7)), ('Ano-mês-dia Hora:minuto:segundo.microsegundo')
natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)
print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)
import csv
with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
final_data

