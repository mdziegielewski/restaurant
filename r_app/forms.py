from django import forms
from django.forms import ModelForm
from .models import *


class AddRestaurantForm(ModelForm):
    class Meta:
        model = RestaurantModel
        exclude = ['reservation']


