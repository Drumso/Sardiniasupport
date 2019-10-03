from django.db import models


class Allergen(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BaseIngredient(models.Model):
    name = models.CharField(max_length=200)
    calories_100_g = models.FloatField(default=0.0)
    saturated_fats = models.FloatField(default=0.0)
    unsaturated_fats = models.FloatField(default=0.0)
    proteins = models.FloatField(default=0.0)
    carbohydrates = models.FloatField(default=0.0)
    measure_unit = models.CharField(max_length=25, default="g")
    allergens = models.ManyToManyField(Allergen)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_ok_lactose = models.BooleanField(default=False)
    is_ok_gluten = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class IngredientInstance(models.Model):
    base_ingredient = models.ForeignKey(BaseIngredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.base_ingredient.name} - {self.amount}{self.base_ingredient.measure_unit}"


class DishComponent(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(IngredientInstance)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    dish_components = models.ManyToManyField(DishComponent)
    allergens = models.ManyToManyField(Allergen)

    def __str__(self):
        return self.name
