import requests
import json




 
class Fipeiterator():
    def __init__(self, id) -> None:
        marca_id = id # ID da marca selecionada
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos'
        headers = {'user-agent': 'MyStudyApp'}

        response = requests.get(url, headers=headers)
        carros = response.json()
        self.modelos = carros['modelos']
        self.current = 0
        self.end = len(self.modelos)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.modelos[self.current]
        self.current += 1
        return result

    
fipe = Fipeiterator('6')
for modelo in fipe:
    print(modelo['nome'])

    