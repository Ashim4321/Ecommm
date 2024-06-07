from django.views import View
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
from store.models.sign_up import SignUp


class OrderView(View):
    def get(self, request):
        customer=request.session.get('id')
        orders=Order.get_order_by_customer(customer)
        orders=orders.reverse()
        return render(request,'order.html',{'orders':orders})