from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('about/',include("about.urls"), name="about-urls"),
    path('map/', include("map.urls"), name="map-urls"),
    path("", include("tobar.urls"), name="tobar-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]
