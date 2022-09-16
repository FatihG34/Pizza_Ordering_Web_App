from django.shortcuts import render,redirect
from pizza.forms import MultiOrderingForm, PizzaForm
from pizza.models import Pizza

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
            note = f'Thanks for ordering! You {make_pizza.cleaned_data["size"]}, {make_pizza.cleaned_data["topping1"]} and {make_pizza.cleaned_data["topping2"]} pizza on its way.'
            pizza_form.save()
        else:
            make_pizza_pk = None
            note = 'Make your choise !'
            return render(request, 'pizza/order.html', {"make_pizza_pk":make_pizza_pk, "pizza_form": pizza_form, "note": note})
    else:
        form = PizzaForm()
        context = {
            "form":form,
            "form_mult": form_mult
        }
        return render(request, 'pizza/order.html', context)



def multi_order(request):
    form = PizzaForm(request.POST or None)
    if form.is_valid():
        return redirect('pizzas')
    context = {
        'form':form,
    }
    return render(request, 'pizza/pizzas.html', context)

def edit_order(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={
        'pizza' : pizza,
        'form': form
    }
    return render(request, 'pizza/edit_order.html', context)