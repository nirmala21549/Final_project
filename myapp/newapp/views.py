# views.py

from django.shortcuts import render
from .models import CarMakeModel, CarSpecifications

def car_make_model_list(request):
    cars = CarMakeModel.objects.all()
    return render(request, 'car_make_model_list.html', {'cars': cars})

def car_specifications_list(request):
    specs = CarSpecifications.objects.all()
    return render(request, 'car_specifications_list.html', {'specs': specs})
