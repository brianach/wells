from django.contrib import admin
from .models import Well


@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display = ('well', 'townland', 'county',
                    'longitude', 'latitude', 'cures')
