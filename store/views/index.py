from django.views import View
from store.models.product import Product
from store.models.category import Category
from django.shortcuts import render,redirect

class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}

        products = Product.get_all_products()
        categories = Category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_product_by_category_id(category_id)
        else:
            products = Product.get_all_products()
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'index.html', context)
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        
        return redirect('homepage')
