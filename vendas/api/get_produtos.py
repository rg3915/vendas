import csv
import json
import ws

# Listar as categorias
with open('fixtures/csv/categorias.csv', 'r') as f:
    r = csv.DictReader(f)
    categorias = [dct for dct in r]
    f.close()

# Pegar 5 produtos de cada categoria
url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1000'
dados = ws.get_data(url)
produtos = json.loads(dados)['results']
print(produtos)

with open('fixtures/csv/produtos.csv', 'w', newline='') as f:
    fieldnames = ['id',
                  'title',
                  'subtitle',
                  'price',
                  'currency_id',
                  'available_quantity',
                  'sold_quantity',
                  'buying_mode',
                  'listing_type_id',
                  'stop_time',
                  'condition',
                  'permalink',
                  'thumbnail',
                  ]
    writer = csv.DictWriter(
        f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()

    for produto in produtos:
        writer.writerow(produto)

    f.close()
