from vendas.core.models import Brand


BRAND_LIST = ('air', 'biork', 'free', 'friday', 'guin', 'king', 'light',
              'plus', 'queen', 'rain', 'seal', 'sky', 'star', 'sub', 'teck',
              'tutu', 'way', 'wpa', 'yant', 'zyka',)

obj = [Brand(brand=val) for val in BRAND_LIST]
Brand.objects.bulk_create(obj)
