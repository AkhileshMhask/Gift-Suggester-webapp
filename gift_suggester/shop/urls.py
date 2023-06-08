from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.home,name="home"),
    path('contactus/',views.contact,name='contactus'),
    path('products/<int:pk>/',views.product_detail,name="product_detail"),
    path('products/list/',views.get_products,name="product_list"),
]


