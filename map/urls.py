from .import views
from django.urls import path

urlpatterns = [
    path('', views.mapper, name='map'),
    path('popup/', views.popup, name='popup'),
]
