from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Dish
# ...

@xframe_options_exempt
class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'all_recipes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Dish.objects.all()

@xframe_options_exempt
def dish_view(request, dish_name):
    dish_set = Dish.objects.filter(unique_name__exact=dish_name)
    if len(dish_set) < 1:
        raise Http404(f"Dish does not exist, possible dishes:", [dish.unique_name for dish in Dish.objects.all()])
    elif len(dish_set) > 1:
        raise AssertionError(f"'Dish.unique_name' should be unique. "
                             f"{len(dish_set)} found instead: {dish_set} ")
    else:
        return render(request, 'recipes/dish.html', {'dish': dish_set[0]})
