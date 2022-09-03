from django.urls import path

from pizza.views import home, order,multi_order

urlpatterns = [
    path("", home, name='home'),
    path("order/", multi_order, name='pizzas'),
    path("order/", order, name='order'),
]