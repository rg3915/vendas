'''
    limbo:
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity or 0 * self.price_sale or 0.00
        super(SaleDetail, self).save(*args, **kwargs)
'''
