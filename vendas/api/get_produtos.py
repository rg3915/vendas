import csv
import json
import ws

# Listar as categorias
with open('fixtures/csv/categorias.csv', 'r') as f:
    r = csv.DictReader(f)
    categorias = [dct for dct in r]
    f.close()

# Gravar produtos em arquivo
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
                  'category_id',
                  ]
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()

    # Pegar os produtos de cada categoria
    for categoria in categorias:
        url = 'https://api.mercadolibre.com/sites/MLB/search?category=%s' \
            % categoria['id']
        dados = ws.get_data(url)
        produtos = json.loads(dados)['results']

        for produto in produtos:
            produto['category_id'] = categoria['id']
            writer.writerow(produto)

    f.close()
