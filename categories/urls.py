from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('add/', views.add_category, name='add_category')
]