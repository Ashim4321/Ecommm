from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static
from store.views.index import Index
from store.views.signup import SignUp
from store.views.home import Home
from store.views.login import Login
from store.views.logout import Logout
from store.views.cart import Cart

urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('home/',Home.as_view(),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
