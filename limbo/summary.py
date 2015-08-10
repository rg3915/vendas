# coding = utf-8

"""
Package containing functions to support the templates.
@author Marcos Thomaz da Silva - marcosthomazs@gmail.com
"""

__author__ = 'Marcos Thomaz da Silva - marcosthomazs@gmail.com'

class Cel(object):
    """
    Class Helper used to store summaries
    """
    value = uval = None
    def __add__(self,val):
        if self.value:
            self.value = self.value +  val
        else:
            self.value = val
        self.uval = val
        return val
    def __str__(self):
        return self.uval
    def __unicode__(self):
        return self.uval
    @property
    def total(self):
        return self.value
    def reset(self):
        self.value = self.uval = None
        return self


class VirtualSummary(object):
    """
    Class to be instantiated in views and used within the templates.
    Usage (only in django templates):
        vs = VirtualSummary()
        
        {{ vs.<your_field_to_summary> }}  = Create a new virtual field to store the summary
        {{ vs.<your_field_to_summary>|add:<value_to_sum> }} = Use the fielter "add" 
                                                              to realize the sum.
        {{ vs.total__<your_field_to_summary> }} = returns the result of the sum
        {{ vs.reset__<your_field_to_summary> }} = reset the sum and 
                                                  return None. Used 
                                                  for realize summary 
                                                  in groups/subgroups
        
        
    Complete Example:
    ================================================
    
    class Sale(models.Model):
    
        product = models.ForeignKey(Product)
        quantity = models.IntegerField()
        value = models.DecimalField('Unitary Value', max_digits=7, decimal_places=2)
        
        @property
        def subtotal(self):
            return self.quantity * self.value
        
        def __unicode__(self):
            return self.product.name
    
    
    def myview(request):
        vtable = VirtualSummary()
        my_sales = Sale.objects.all()
        return render(request, 'your_template.html' , locals())
        
    
    ======= your_template.html =====
    <html>
        <body>
            <table>
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Quantity</th><!-- {{ vtable.qty }} -->
                        <th>Un.Value</th><!-- {{ vtable.unval }} -->
                        <th>Subtotal</th><!-- {{ vtable.subtot }} -->
                    </tr>
                </thead>
                <tbody>
                    {% for sale in my_sales %}
                    <tr>
                        <td>{{ sale.product }}</td>
                        <td>{{ vtable.qty|add:sale.quantity }}</td>
                        <td>{{ vtable.unval|add:sale.value }}</td>
                        <td>{{ vtable.subtot|add:sale.subtotal }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
                <tfooter>
                    <tr>
                        <th>Total</th>
                        <th>{{ vtable.total__qty }}</th>                        
                        <th>{{ vtable.total__unval }}</th>                        
                        <th>{{ vtable.total__subtot }}</th>                        
                    </tr>
                </tfooter>
            </table>
        </body>
    </html>
    """
    
    __values = {}
    
    # TODO Another operations: Subtraction, Average and Median
    
    def __getattr__(self, name):
        if name[:2] == '__' :
            return super(VirtualSummary, self).__getattr__(name)
        elif '__' in name:
            data = name.split('__')
            if data[0] == 'total':
                return self.__values[data[1]].total
            elif data[0] == 'reset':
                return self.__values[data[1]].reset()
        if not (name in self.__values):
            self.__values[name] = Cel()
        return self.__values[name]
