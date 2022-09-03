from django.shortcuts import render,redirect
from pizza.forms import MultiOrderingForm, PizzaForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def ordering_pizza(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form': form
    }
    return render(request, 'pizza/order.html', context)

def multi_order(request):
    form = PizzaForm()
    form_multi = MultiOrderingForm(request.POST or None)
    if form_multi.is_valid():
        form_multi.save()
        return redirect('home')
    context = {
        'form' : form,
        'form_multi': form_multi
    }
    return render(request, 'pizza/pizzas.html', context)