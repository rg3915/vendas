from .models import Customer, Category, Product
import django_filters


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['product', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['product'].extra.update(
            {'empty_label': 'All products'})
