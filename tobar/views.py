from django.shortcuts import render
from django.views import generic, View
from map.models import Well


class WellDetail(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all data from the Well model
        well_data = Well.objects.values('well', 'townland', 'county', 'cures')
        well_data_list = list(well_data)
        # Pass the well_data to the specified template
        return render(request, 'well.html', context={'well_data': well_data_list})
        # for record in well_data:
        #    addr_one = record['townland']
        # return render(request, 'well.html', context={'addr_one': addr_one})
