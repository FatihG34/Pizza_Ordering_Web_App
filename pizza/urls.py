from django.urls import path

from pizza.views import home, order,multi_order

urlpatterns = [
    path("", home, name='home'),
    path("order/", order, name='order'),
    path("pizzas/", multi_order, name='pizzas'),
]