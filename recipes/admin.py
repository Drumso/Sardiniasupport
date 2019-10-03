from django.contrib import admin

from .models import Dish, DishComponent, BaseIngredient, IngredientInstance, Allergen

admin.site.register(Dish)
admin.site.register(DishComponent)
admin.site.register(BaseIngredient)
admin.site.register(IngredientInstance)
admin.site.register(Allergen)
