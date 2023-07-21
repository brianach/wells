from .import views
from django.urls import path
#import tobar.views

urlpatterns = [
    path('', views.mapper, name='map'),
    path('popup/', views.popup, name='popup'),
    #path('<int:pk>', tobar.views.WellDetail.as_view(), name='well_detail'),
]
