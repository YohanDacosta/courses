from django.urls import path
from . import views

urlpatterns = [
    path('index', views.getIndex, name='index'),
]
