from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RegisterForm, LoginForm, AddRecipeForm, ModifyRecipeForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            if password_1 != password_2:
                ctx = {
                    'form': form,
                    'error': "Passwords are different. Fill the form once again",
                }
                return render(request, 'register.html', ctx)
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, email=email, password=password_1)
            login(request, user)
            return HttpResponseRedirect('/user_recipes')
        return render(request, 'register.html', {'form': form})


class LogInView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user_recipes')
            else:
                return render(
                    request, 'login.html',
                    {'form': form,
                     'error': 'Invalid username or password.'})


class LogOutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('all_recipes')


class AddRecipeView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddRecipeForm(initial={'author': request.user})
        return render(request, 'add_recipe.html', {'form': form})

    def post(self, request):
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user_recipes')
        return render(request, 'add_recipe.html', {'form': form})


class ModifyRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = ModifyRecipeForm
    template_name = 'modify_recipe.html'

    def form_valid(self, form):
        form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('recipe_details', kwargs={'recipe_id': self.object.id})


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('user_recipes')


class ShowUserRecipesView(LoginRequiredMixin, View):

    def get(self, request):
        author = request.user
        recipes = Recipe.objects.filter(author=author).order_by('title')
        return render(request, 'user_recipes.html', {'recipes': recipes,
                                                     'author': author})


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_details.html'


class RecipesView(View):

    def get(self, request):
        recipes = Recipe.objects.order_by('title').all()
        return render(request, 'all_recipes.html', {'recipes': recipes})


class SeasonRecipesView(View):

    def get(self, request, season):
        season = int(season)
        if season == 1:
            recipes = Recipe.objects.filter(recipe_season=1).order_by('title').all()
        elif season == 2:
            recipes = Recipe.objects.filter(recipe_season=2).order_by('title').all()
        elif season == 3:
            recipes = Recipe.objects.filter(recipe_season=3).order_by('title').all()
        elif season == 4:
            recipes = Recipe.objects.filter(recipe_season=4).order_by('title').all()
        else:
            return HttpResponseBadRequest('Page doesn\'t exist')
        return render(request, 'season_recipes.html', {'season': season,
                                                       'recipes': recipes})


class CategoryRecipesView(View):

    def get(self, request, category):
        category = int(category)
        if category == 1:
            recipes = Recipe.objects.filter(category=1).order_by('title').all()
        elif category == 2:
            recipes = Recipe.objects.filter(category=2).order_by('title').all()
        elif category == 3:
            recipes = Recipe.objects.filter(category=3).order_by('title').all()
        elif category == 4:
            recipes = Recipe.objects.filter(category=4).order_by('title').all()
        elif category == 5:
            recipes = Recipe.objects.filter(category=5).order_by('title').all()
        else:
            return HttpResponseBadRequest('Page doesn\'t exist')
        return render(request, 'category_recipes.html', {'category': category,
                                                         'recipes': recipes})






