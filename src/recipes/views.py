from django.shortcuts import render
from django.views.generic import ListView, DetailView #to display lists and details
from .models import Recipe #to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin #to protect class-based view

# Create your views here.
# def recipes_home(request):
#    return render(request, 'recipes/recipes_home.html')

class HomeRecipeListView(ListView):             #class-based view
   model = Recipe                               #specify model
   template_name = 'recipes/recipes_home.html'  #specify template 

class RecipeListView(LoginRequiredMixin, ListView):           #class-based “protected” view
   model = Recipe                         #specify model
   template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based “protected” view
   model = Recipe                                       #specify model
   template_name = 'recipes/detail.html'                 #specify template