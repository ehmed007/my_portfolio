from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('download/', views.download_cv, name='download_cv'),
]
