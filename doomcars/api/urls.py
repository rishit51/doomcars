from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.home,name='home_view'),
    path('cars/',views.cars,name='cars_all')
]

