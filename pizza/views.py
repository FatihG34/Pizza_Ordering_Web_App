from django.shortcuts import render,redirect
from pizza.forms import PizzaForm

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