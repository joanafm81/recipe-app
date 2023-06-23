from django.db import models
from ingredients.models import Ingredient
#from recipe_ingredients.models import Recipe_ingredient

# Create your models here.
difficulty_choices = (
  ('easy', 'Easy'),
  ('medium', 'Medium'),
  ('intermediate', 'Intermediate'),
  ('hard', 'Hard'),
)

class Recipe(models.Model):
  name = models.CharField(max_length=50)
  ingredients = models.ManyToManyField(Ingredient, through='recipe_ingredients.Recipe_ingredient', through_fields=('recipe', 'ingredient'))
  cooking_time = models.IntegerField(help_text='Cooking time in minutes')
  difficulty = models.CharField(max_length=20, choices=difficulty_choices)

  def __str__(self):
    return str(self.name)