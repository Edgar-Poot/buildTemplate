from django.urls import path
from .views import regresion_template

urlpatterns = [
    path("regresion/", regresion_template, name="regresion_template"),
]
