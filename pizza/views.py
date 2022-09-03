from django.shortcuts import render,redirect
from pizza.forms import MultiOrderingForm, PizzaForm
from pizza.models import Pizza

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    form = PizzaForm(request.POST or None)
    form_mult = MultiOrderingForm(request.POST or None)
    if form_mult.is_valid():
        form_mult.save()
        return redirect('pizzas')
    elif form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form' : form,
        'form_mult': form_mult
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