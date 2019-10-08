from django.db import models
from django.utils import timezone

from recipes.measures import Measures


def capital_spaced_from_lower_underscored(name: str) -> str:
    return name.capitalize().replace("_", " ")


class AbstractIngredient(models.Model):
    class Meta:
        abstract = True

    unique_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return capital_spaced_from_lower_underscored(self.unique_name)


class Allergen(AbstractIngredient):
    pass

class BaseIngredient(AbstractIngredient):
    calories_100_g = models.FloatField(default=0.0)
    saturated_fats = models.FloatField(default=0.0)
    unsaturated_fats = models.FloatField(default=0.0)
    proteins = models.FloatField(default=0.0)
    carbohydrates = models.FloatField(default=0.0)
    sugars = models.FloatField(default=0.0)
    allergens = models.ManyToManyField(Allergen, blank=True)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_ok_lactose = models.BooleanField(default=False)
    is_ok_gluten = models.BooleanField(default=False)
    is_low_lactose = models.BooleanField(default=False)


class IngredientInstance(models.Model):
    base_ingredient = models.ForeignKey(BaseIngredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    measure_type = models.CharField(max_length=25, default="weight", blank=True, choices=Measures.allowed_measure_types)
    measure_unit_code = models.CharField(max_length=25, default="g", blank=True)

    def __str__(self):
        name = f"{self.base_ingredient.get_name()}, "
        if self.measure_type != "extra":
            name += f"{self.amount}{self.measure_unit_code}"
        else:
            name += f"{self.measure_unit_code}"
        return name


class DishComponent(models.Model):
    unique_name = models.CharField(unique=True, max_length=200)
    custom_name = models.CharField(max_length=200, default="")
    ingredients = models.ManyToManyField(IngredientInstance)
    required_time_min = models.IntegerField(default=0)

    def __str__(self):
        return capital_spaced_from_lower_underscored(self.unique_name)

    def get_name(self):
        name = self.custom_name if self.custom_name != "" else self.unique_name
        return capital_spaced_from_lower_underscored(name)


class Dish(models.Model):
    unique_name = models.CharField(unique=True, max_length=200)
    dish_components = models.ManyToManyField(DishComponent)
    energy = models.IntegerField(default=0)
    servings = models.IntegerField(default=4)
    difficulty_levels = [
        ("easy", "easy"),
        ("medium", "medium"),
        ("advanced", "advanced"),
        ("hard", "hard"),
    ]
    difficulty = models.CharField(max_length=25, default="medium", blank=True, choices=difficulty_levels)

    def __str__(self):
        return self.name()

    def name(self):
        return capital_spaced_from_lower_underscored(self.unique_name)
