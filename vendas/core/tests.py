from django.test import TestCase, Client

from .models import Category


# Create your tests here.
class CategoryTest(TestCase):

    def test_defaults(self):
        category = Category(id='AAA2345')
        self.assertEquals(category.id, 'AAA2345')
        self.assertEquals(category.category, '')

    def test_saving_and_retrieving_categories(self):
        category_1 = Category(id='AAA1111', category='Category 1')
        category_1.save()
        category_2 = Category(id='BBB2222', category='Category 2')
        category_2.save()
        category_3 = Category(id='CCC3333', category='Category 3')
        category_3.save()

        saved_categories = Category.objects.all()
        self.assertEquals(saved_categories.count(), 3)

        saved_category_1 = saved_categories[0]
        saved_category_2 = saved_categories[1]
        saved_category_3 = saved_categories[2]
        self.assertEquals(saved_category_1.id, 'AAA1111')
        self.assertEquals(saved_category_2.id, 'BBB2222')
        self.assertEquals(saved_category_3.id, 'CCC3333')
