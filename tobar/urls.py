from .import views
from django.urls import path

urlpatterns = [
    path('', views.WellDetail.as_view(), name='home'),
]
