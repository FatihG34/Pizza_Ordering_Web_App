from django.urls import path

from pizza.views import home, ordering_pizza

urlpatterns = [
    path("", home, name='home'),
    path("order/", ordering_pizza, name='order'),
]