from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DishComponent(models.Model):
    name = models.CharField(max_length=200)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return self.name


class BaseIngredient(models.Model):
    name = models.CharField(max_length=200)
    dish_components = models.ManyToManyField(DishComponent)
    calories_100_g = models.FloatField(default=0.0)
    measure_unit = models.CharField(max_length=25, default="g")

    def __str__(self):
        return self.name


class IngredientInstance(models.Model):
    base_ingredient = models.ForeignKey(BaseIngredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.base_ingredient.name} - {self.amount}{self.base_ingredient.measure_unit}"



