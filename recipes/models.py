from django.db import models


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
    measure_unit = models.CharField(max_length=25, default="g")
    allergens = models.ManyToManyField(Allergen, default=None)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_ok_lactose = models.BooleanField(default=False)
    is_ok_gluten = models.BooleanField(default=False)


class IngredientInstance(models.Model):
    base_ingredient = models.ForeignKey(BaseIngredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.base_ingredient.get_name()} - {self.amount}{self.base_ingredient.measure_unit}"


class DishComponent(models.Model):
    unique_name = models.CharField(unique=True, max_length=200)
    ingredients = models.ManyToManyField(IngredientInstance)

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return capital_spaced_from_lower_underscored(self.unique_name)


class Dish(models.Model):
    unique_name = models.CharField(unique=True, max_length=200)
    dish_components = models.ManyToManyField(DishComponent)

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return capital_spaced_from_lower_underscored(self.unique_name)
