# Generated by Django 2.2.5 on 2019-10-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20191006_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('easy', 'easy'), ('medium', 'medium'), ('advanced', 'advanced'), ('hard', 'hard')], default='medium', max_length=25),
        ),
        migrations.AddField(
            model_name='dish',
            name='energy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dish',
            name='servings',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='dishcomponent',
            name='required_time_min',
            field=models.IntegerField(default=0),
        ),
    ]
