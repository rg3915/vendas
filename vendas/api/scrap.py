import csv
import json
import ws


url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1648'
dados = ws.get_data(url)
produtos = json.loads(dados)['results']


with open('produtos.csv', 'w', newline='') as f:
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
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for produto in produtos:
        writer.writerow(produto)
