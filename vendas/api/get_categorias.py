import csv
import json
import ws

# Listar as categorias

url = 'https://api.mercadolibre.com/sites/MLB/categories'
dados = ws.get_data(url)
categorias = json.loads(dados)


with open('fixtures/csv/categorias.csv', 'w', newline='') as f:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()

    for categoria in categorias:
        writer.writerow(categoria)
