from django import forms
from django.forms import ModelForm
from .models import RECIPE_SEASON, Recipe, CATEGORIES


class RegisterForm(forms.Form):
    username = forms.CharField(label='Name:')
    email = forms.EmailField(label='E-mail:')
    password_1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_2 = forms.CharField(widget=forms.PasswordInput, label='Repeat password')


class LoginForm(forms.Form):
    username = forms.CharField(label='Name:')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class AddRecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {'author': forms.HiddenInput, }


class ModifyRecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {'author': forms.HiddenInput, }

