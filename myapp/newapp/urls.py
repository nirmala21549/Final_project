# urls.py (inside your app's directory)

from django.urls import path
from . import views

urlpatterns = [
    path('car-make-models/', views.car_make_model_list, name='car_make_model_list'),
    path('car-specifications/', views.car_specifications_list, name='car_specifications_list'),
]
