from django.shortcuts import render, redirect
from django.views import View

from r_app.forms import *
from r_app.models import *


class RestaurantView(View):
    def get(self, request):
        restaurants = RestaurantModel.objects.all()

        return render(request,
                      "r_app/restaurant_list.html",
                      {"restaurants": restaurants})

    def post(self, request):
        pass


class AddRestaurantView(View):
    def get(self, request):
        form = AddRestaurantForm()
        return render(request,
                      "r_app/add_restaurant.html",
                      {"form": form})

    def post(self, request):
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            house_number = form.cleaned_data['house_number']
            RestaurantModel.objects.create(name=name, city=city,
                                           street=street, house_number=house_number)
            return redirect('/home')
        return render(request,
                      "r_app/add_restaurant.html",
                      {"form": form})
