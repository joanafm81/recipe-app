from django.test import TestCase
from .models import Recipe, Ingredient

# Create your tests here.
class RecipeModelTest(TestCase):
  def setUpTestData():
    # Set up non-modified objects used by all test methods
    ingredient = Ingredient.objects.create(name='Lemons')
    recipe = Recipe.objects.create(name='Lemonade', cooking_time=5, difficulty='Intermediate')
    recipe.ingredients.add(ingredient)

  def test_ingredient_in_recipe(self):
    recipe = Recipe.objects.get(id=1)
    ingredient = recipe.ingredients.get(id=1)
    self.assertEqual(ingredient.name, 'Lemons')

  def test_recipe_name_max_length(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'name' field and use it to query its max_length
    max_length = recipe._meta.get_field('name').max_length

    # Compare the value to the expected result i.e. 50
    self.assertEqual(max_length, 50)

  def test_difficulty_max_length(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'difficulty' field and use it to query its max_length
    max_length = recipe._meta.get_field('difficulty').max_length

    # Compare the value to the expected result i.e. 20
    self.assertEqual(max_length, 20)

  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    #get_absolute_url() should take you to the detail page of recipe #1
    #and load the URL /recipes/list/1
    self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

  