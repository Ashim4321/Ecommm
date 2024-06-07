from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.sign_up import SignUp
from .models.orders import Order

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product','desc','image','price','category']
admin.site.register(Category)
admin.site.register(SignUp)
admin.site.register(Order)
