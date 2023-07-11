from django.shortcuts import render
from .models import Well
import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def mapper(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    wells = list(Well.objects.all().values())
    # print("Wells: ", wells)
    transposed_wells = []
    for well in wells:
        output = {
            "type": "Feature",
            "properties": {"title": well['well']},
            "geometry": {
                "coordinates": [float(well['longitude']), float(well['latitude'])],
                "type": "Point"
            }
        }
        transposed_wells.append(output)
        # print(output)

    # print(transposed_wells)
    json_wells = json.dumps(list(transposed_wells), cls=DjangoJSONEncoder)
    # print(json_wells)
    return render(request, 'map.html', {'mapbox_access_token': mapbox_access_token, 'wells': json_wells})


def popup(request):
    title = request.GET.get('title')
    coordinates = request.GET.get('coordinates')
    data = {'title': title, 'content': coordinates}
    # Render the popup template with the data
    return render(request, 'popup.html', data)
