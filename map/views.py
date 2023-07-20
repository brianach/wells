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
        # post_title = [post.title for post in posts]
        # post_content = [post.content for post in posts]
        post_data = [
            {
                "title": post.title,
                # Generate the URL for 'post_detail' view
                "url": reverse('post_detail', args=[post.id]),
                "content": post.content,
            }
            for post in posts
        ]

        output = {
            "type": "Feature",
            "properties": {
                "title": well['well'],
                "post": post_data,

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
    coordinates = request.GET.get('coordinates')
    data = {'title': title, 'content': coordinates}
    # Render the popup template with the data
    return render(request, 'popup.html', data)
