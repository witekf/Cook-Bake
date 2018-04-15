from django.db import models
from django.contrib.auth.models import User

# Create your models here.


RECIPE_SEASON = (
    (1, 'SPRING'),
    (2, 'SUMMER'),
    (3, 'AUTUMN'),
    (4, 'WINTER'),
)


CATEGORIES = (
    (1, 'STARTER'),
    (2, 'SOUP'),
    (3, 'MAIN DISH'),
    (4, 'PASTA'),
    (5, 'BAKING RECIPE'),
)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    photo = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, related_name='your_recipes')
    recipe_season = models.IntegerField(choices=RECIPE_SEASON)
    category = models.IntegerField(choices=CATEGORIES)

    """def __str__(self):
        return '{} {} /n {} ({}) /n Składniki: /n {} /n {} /n {}'.format(self.photo, self.rank, self.title, self.author,
                                                                         self.ingredients, self.description,
                                                                         self.recipe_season)"""
