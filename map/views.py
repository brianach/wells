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
        try:
            # Fetch related 'Post' records for each 'Well'
            posts = Post.objects.filter(well=well['id'])
            post_slug = [post.slug for post in posts]
            post_excerpt = [post.excerpt for post in posts]
        except ObjectDoesNotExist:
            # Handle the case when no related 'Post' record is found
            post_slug = None
            post_excerpt = []

        output = {
            "type": "Feature",
            "properties": {
                "title": well['well'],
                "post_excerpt": post_excerpt,
                "post_slug": post_slug,
            },
            "geometry": {
                "coordinates": [float(well['longitude']), float(well['latitude'])],
                "type": "Point"
            }
        }
        transposed_wells.append(output)

    json_wells = json.dumps(list(transposed_wells), cls=DjangoJSONEncoder)

    map_page_class = True  # Set specific class on the map page header and footer
    return render(request, 'map.html', {'map_page_class': map_page_class, 'mapbox_access_token': mapbox_access_token, 'wells': json_wells})


def popup(request):
    title = request.GET.get('title')
    post_slug = request.GET.get('post_slug')
    excerpt = request.GET.get('excerpt')
    coordinates = request.GET.get('coordinates')
    post_url = reverse('post_detail', args=[post_slug])

    # if post_slug != 'undefined':
    #    post_url = reverse('post_detail', args=[post_slug])
    # else:
    #    post_url = '#'

    data = {
        'title': title,
        'excerpt': excerpt,
        'post_url': post_url,
        'coordinates': coordinates,
    }

    return render(request, 'popup.html', data)
