from django.contrib import admin
from django.urls import path, include
from map.views import mapper, popup


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("tobar.urls"), name="tobar-urls"),
    path('summernote/', include('django_summernote.urls')),
    # path('wells/', include('tobar.urls'), name='tobar'),
    path('map/', mapper, name='map'),
    path('map/popup/', popup, name='popup'),
]
