from django.views import View
from django.shortcuts import redirect,render

class SignUp(View):
    def get(self,request):
        return render(request,'sign_up.html')

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        sign = SignUp(name=name, email=email, password=password, address=address)
        sign.save()

        return render(request, 'sign_up.html')