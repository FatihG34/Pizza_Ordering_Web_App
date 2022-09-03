from django import forms
from pizza.models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields= ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping_1', 'topping2':'Topping_2', 'size': 'Size'}


class MultiOrderingForm(forms.Form):
    number=forms.IntegerField(required=False)