from urllib.parse import urlparse
from django.urls import path
from . import views

app_name='fronted'

urlpatterns = [
    # path('',views.home,name='home')#when someone ask for domain name/ we pass view.home
    path('',views.HomeView.as_view(),name='home'),
    path('product/<slug>/',views.ProductDetailView.as_view(),name='detail'),
    # path('test/',views.testpage,name='test')
    path('add-to-cart/<slug>/',views.add_to_cart,name='add-to-cart')
]
