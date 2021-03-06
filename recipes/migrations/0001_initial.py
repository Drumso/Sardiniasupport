# Generated by Django 2.2.5 on 2019-10-03 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BaseIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories_100_g', models.FloatField(default=0.0)),
                ('saturated_fats', models.FloatField(default=0.0)),
                ('unsaturated_fats', models.FloatField(default=0.0)),
                ('proteins', models.FloatField(default=0.0)),
                ('carbohydrates', models.FloatField(default=0.0)),
                ('measure_unit', models.CharField(default='g', max_length=25)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_ok_lactose', models.BooleanField(default=False)),
                ('is_ok_gluten', models.BooleanField(default=False)),
                ('allergens', models.ManyToManyField(to='recipes.Allergen')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('base_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.BaseIngredient')),
            ],
        ),
        migrations.CreateModel(
            name='DishComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.ManyToManyField(to='recipes.IngredientInstance')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('allergens', models.ManyToManyField(to='recipes.Allergen')),
                ('dish_components', models.ManyToManyField(to='recipes.DishComponent')),
            ],
        ),
    ]
