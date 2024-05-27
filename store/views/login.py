from django.views import View
from django.shortcuts import render,redirect
from store.models.sign_up import SignUp

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = SignUp.objects.get(email=email)
        if (user.password == password):
            request.session['user'] = user.name
            request.session['id'] = user.id
            return redirect('homepage')

        return render(request, 'login.html')