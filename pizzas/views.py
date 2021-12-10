from django.shortcuts import render
from . models import Pizza

# Create your views here.
def index(request):
    #The home page for the pizzeria
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizza.html',context)