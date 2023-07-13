from django.urls import path
from webapp import views

urlpatterns=[
    path('home_page', views.home_page),
    path('products', views.products),
    path('add_to_cart', views.add_to_cart.as_view()),
    path('view_cart', views.view_cart),
    path('checkout',views.checkout),
    path('add_address', views.add_address),
    path('proceed_to_payment', views.proceed_to_payment),
    path('payment', views.payment),
    path('my_order', views.my_order),

]