"""cookingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cookbook.views import RegisterView, LogInView, LogOutView, AddRecipeView, ModifyRecipeView, RecipesView, ShowUserRecipesView, SeasonRecipesView, CategoryRecipesView, RecipeDetailView, DeleteRecipeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^login', LogInView.as_view(), name='login'),
    url(r'^logout', LogOutView.as_view(), name='logout'),
    url(r'^add_recipe', AddRecipeView.as_view(), name='add_recipe'),
    url(r'^modify_recipe/(?P<pk>(\d)+)$', ModifyRecipeView.as_view(), name='modify_recipe'),
    url(r'^recipe_details/(?P<pk>(\d)+)$', RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^delete_recipe/(?P<pk>(\d)+)$', DeleteRecipeView.as_view(), name='delete_recipe'),
    url(r'^all_recipes', RecipesView.as_view(), name='recipes'),
    url(r'^user_recipes', ShowUserRecipesView.as_view(), name='user_recipes'),
    url(r'^season_recipes/(?P<season>(\d)+)$', SeasonRecipesView.as_view(), name='season_recipes'),
    url(r'^category_recipes/(?P<category>(\d)+)$', CategoryRecipesView.as_view(), name='category_recipes')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
