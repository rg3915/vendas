from random import randint
from vendas.core.models import Customer, Seller, Sale, SaleDetail, Product

REPEAT = 120
qcustomers = Customer.objects.count()
qsellers = Seller.objects.count()
qproducts = Product.objects.count()

for i in range(REPEAT):
    c = randint(1, qcustomers)
    customer = Customer.objects.get(pk=c)
    s = randint(1, qsellers)
    seller = Seller.objects.get(pk=s)
    obj = Sale(
        customer=customer,
        seller=seller,
    )
    obj.save()
    for j in range(randint(1, 10)):
        sale = Sale.objects.get(pk=obj.pk)
        p = randint(1, qproducts)
        product = Product.objects.get(pk=p)
        quantity = randint(1, 50)
        price_sale = product.price
        ipi_sale = product.ipi
        sd = SaleDetail(
            sale=sale,
            product=product,
            quantity=quantity,
            price_sale=price_sale,
            ipi_sale=ipi_sale,
        )
        sd.save()


print('%d Vendas salvo com sucesso.' % REPEAT)
