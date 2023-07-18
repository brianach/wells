from django.contrib import admin
from .models import Well


# Register the well table view in django admin
@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display = ('well', 'townland', 'county', 'cures',)
    search_fields = ['well']
