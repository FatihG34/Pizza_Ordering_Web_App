from django.shortcuts import render, redirect
from pizza.forms import MultiOrderingForm, PizzaForm
from pizza.models import Pizza
from django.contrib import messages
from django.forms import formset_factory

# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form_mult = MultiOrderingForm()
    if request.method == 'POST':
        pizza_form = PizzaForm(request.POST)
        if pizza_form.is_valid():
            make_pizza = pizza_form.save()
            make_pizza_pk = make_pizza.id

            size = pizza_form.cleaned_data.get('size')
            topping1 = pizza_form.cleaned_data.get('topping1')
            topping2 = pizza_form.cleaned_data.get('topping2')
            messages.success(
                request, f"Thanks for ordering! {size},{topping1} and {topping2} pizza is on its way!")
            make_pizza = PizzaForm()
            return render(request, 'pizza/order.html', {'created_pizza_pk': make_pizza_pk, 'pizzaform': pizza_form, 'multiple_form': form_mult})
        else:
            make_pizza_pk = None
            messages.warning(request, 'Pizza order failed, try again!')
            return render(request, 'pizza/order.html', {'created_pizza_pk': make_pizza_pk, 'pizzaform': pizza_form, 'multiple_form': form_mult})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {"pizzaform": form,"multiple_form": form_mult})


def multi_order(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiOrderingForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data.get(
            'number')
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
                messages.success(request, 'Pizzas have been ordered!')
        else:
            messages.warning(
                request, 'Order was not created, please try again')
        return render(request, 'pizza/pizzas.html', {'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order has been updated.')
            return render(request, 'pizza/edit_order.html', {
                'pizza': pizza,
                'form': form
            })
    context = {
        'pizza': pizza,
        'form': form
    }
    return render(request, 'pizza/edit_order.html', context)
