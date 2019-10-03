from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Dish
# ...

def index(request):
    return HttpResponse("output")

def dish_view(request, dish_id):
    try:
        dish = Dish.objects.get(pk=dish_id)
    except Dish.DoesNotExist:
        raise Http404("Dish does not exist")
    return render(request, 'recipes/dish.html', {'dish': dish})


