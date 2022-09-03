from dataclasses import fields
from django import forms
from pizza.models import Pizza, Quant


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields= ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping_1', 'topping2':'Topping_2', 'size': 'Size'}


class MultiOrderingForm(forms.Form):
    class Meta:
        model:Quant
        fields='__all__'
        