from django.urls import path

from pizza.views import home, ordering_pizza,multi_order

urlpatterns = [
    path("", home, name='home'),
    path("order/", ordering_pizza, name='order'),
    path("multiorder/", multi_order, name='multiorder'),
]