from django.urls import path
from .views import RecipeListView, RecipeDetailView, HomeRecipeListView

app_name = 'recipes'

urlpatterns = [
   path('', HomeRecipeListView.as_view(), name='home'),
   path('recipes/list/', RecipeListView.as_view(), name='list'),
   path('recipes/list/<pk>', RecipeDetailView.as_view(), name='detail'),
]