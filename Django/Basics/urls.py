from django.urls import path
from Basics import views
urlpatterns = [
    path('Largest/',views.Largest,name="Largest"),
    path('Calculator/',views.Calculator,name="Calculator"),
    path('Salarycal/',views.Salarycal,name="Salarycal")
]