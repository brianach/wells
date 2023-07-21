from django.shortcuts import render
from .models import Well
from tobar.models import Post
import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse


def mapper(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    wells = list(Well.objects.all().values())

    transposed_wells = []
    for well in wells:
        # Fetch related 'Post' records for each 'Well'
        posts = Post.objects.filter(well=well['id'])
        post_slug = [post.slug for post in posts]
        post_content = [post.content for post in posts]

        output = {
            "type": "Feature",
            "properties": {
                "title": well['well'],
                "post_content": post_content,
                "post_slug": post_slug,
            },
            "geometry": {
                "coordinates": [float(well['longitude']), float(well['latitude'])],
                "type": "Point"
            }
        }
        transposed_wells.append(output)

    json_wells = json.dumps(list(transposed_wells), cls=DjangoJSONEncoder)

    return render(request, 'map.html', {'mapbox_access_token': mapbox_access_token, 'wells': json_wells})


def popup(request):
    title = request.GET.get('title')
    post_slug = request.GET.get('post_slug')
    coordinates = request.GET.get('coordinates')
    post_url = reverse('post_detail', args=[post_slug])

    data = {
        'title': title,
        'post_slug': post_slug,
        'coordinates': coordinates,
        'post_url': post_url,
    }

    return render(request, 'popup.html', data)
