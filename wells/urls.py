from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include("map.urls"), name="map-urls"),
    #path('tobar/', include(('tobar.urls', 'tobar'), namespace='tobar')),
    path("", include("tobar.urls"), name="tobar-urls"),
    path('summernote/', include('django_summernote.urls')),
]
