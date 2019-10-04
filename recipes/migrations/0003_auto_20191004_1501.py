# Generated by Django 2.2.5 on 2019-10-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20191004_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergen',
            name='unique_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='baseingredient',
            name='unique_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='unique_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='dishcomponent',
            name='unique_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
