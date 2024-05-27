from django.db import models
from store.models.category import Category

class Product(models.Model):
    product=models.CharField(max_length=50)
    desc=models.TextField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price=models.IntegerField()
    image=models.ImageField(upload_to='files/')

    def __str__(self):
        return self.product

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
