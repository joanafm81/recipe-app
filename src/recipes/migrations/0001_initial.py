# Generated by Django 4.2.2 on 2023-06-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe_ingredients', '0001_initial'),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cooking_time', models.IntegerField(help_text='Cooking time in minutes')),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('intermediate', 'Intermediate'), ('hard', 'Hard')], max_length=20)),
                ('ingredients', models.ManyToManyField(through='recipe_ingredients.Recipe_ingredient', to='ingredients.ingredient')),
            ],
        ),
    ]
