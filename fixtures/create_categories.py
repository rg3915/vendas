import csv

from vendas.core.models import Category


with open('fixtures/csv/categorias.csv', 'r') as f:
    saved_categories_counter = 0
    for row in csv.DictReader(f):
        category = Category(id=row['id'],
                            category=row['name'])
        try:
            category.save()
            saved_categories_counter += 1
        except:
            print('Registro existente.')
    f.close()
