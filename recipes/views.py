from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Dish
# ...

def index(request):
    return HttpResponse("output")

def dish_view(request, dish_name):
    dish_set = Dish.objects.filter(unique_name__exact=dish_name)
    if len(dish_set) < 1:
        raise Http404("Dish does not exist")
    elif len(dish_set > 1):
        raise AssertionError(f"'Dish.unique_name' should be unique. "
                             f"{len(dish_set)} found instead: {dish_set} ")
    else:
        return render(request, 'recipes/dish.html', {'dish': dish_set[0]})
