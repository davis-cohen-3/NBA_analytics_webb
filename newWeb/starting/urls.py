from django.urls import path
from starting import views

urlpatterns = [
    path('', views.starting, name='starting'),
]