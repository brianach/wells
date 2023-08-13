from django.contrib import admin
from django.urls import path, include
from .views import err400, err403, err404, err405,  err500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include("about.urls"), name="about-urls"),
    path('map/', include("map.urls"), name="map-urls"),
    path("", include("tobar.urls"), name="tobar-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]

# Custom error views
handler400 = 'wells.views.err400'
handler403 = 'wells.views.err403'
handler404 = 'wells.views.err404'
handler405 = 'wells.views.err405'
handler500 = 'wells.views.err500'
