mapboxgl.accessToken = 'pk.eyJ1IjoiYm9jdWFsYWluIiwiYSI6ImNsamJwOGJ4MjI4cjMzbm54YzBmeTd0ZHYifQ.mdnhGzOR0zbyhc5-SUE4Pg';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-9.08, 52.91],
    zoom: 9.5
});

/* Load map and custom icons */

//var image = 'https://res.cloudinary.com/dpii8ntba/image/upload/c_scale,w_32/v1687818472/locomo/i_well_g6wr4h.png';

map.on('load', () => {

    // Add an image to use as a custom marker
    map.loadImage('/static/img/h_well.png',
        (error, image) => {
            if (error) throw error;
            map.addImage('custom-marker', image);
        }
    );

    var mapElement = document.getElementById('map');
    var wells = mapElement.getAttribute('data-wells');

    // Add a GeoJSON source with the retrieved data
    map.addSource('points', {
        'type': 'geojson',
        'data': {
            'type': 'FeatureCollection',
            'features': JSON.parse(wells)
        }
    });

    // Add a symbol layer
    map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'points',
        'layout': {
            'icon-image': 'custom-marker',
            // get the title name from the source's "title" property
            'text-field': ['get', 'well'],
            'text-font': [
                'Open Sans Semibold',
                'Arial Unicode MS Bold'
            ],
            'text-offset': [0, 1.25],
            'text-anchor': 'top'
        }
    });

    // Load popup when location clicked
    map.on('click', 'points', function (e) {

        var title = e.features[0].properties.title;
        var post_slug = e.features[0].properties.post_slug.replace(/[\[\]""]/g, '');
        var coordinates = e.features[0].geometry.coordinates.slice();
        var r_coordinates = coordinates.slice().reverse(); //for exporting to google maps
        var url = 'popup?title=' + encodeURIComponent(title) + '&post_slug=' + encodeURIComponent(post_slug) + '&coordinates=' + encodeURIComponent(r_coordinates.map(coord => Math.ceil(coord * 100000) / 100000).join(','));
        var xhr = new XMLHttpRequest();

        xhr.open('GET', url);
        xhr.onload = function () {
            if (xhr.status === 200) {
                var data = xhr.responseText;
                new mapboxgl.Popup().setLngLat(coordinates).setHTML(data).addTo(map);
            } else {
                console.error('Request failed.  Returned status of ' + xhr.status);
            }
        };
        xhr.send();
    });

    // Change the cursor to a pointer when over point
    map.on('mouseenter', 'points', function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back to a pointer after leaving point
    map.on('mouseleave', 'points', function () {
        map.getCanvas().style.cursor = '';
    });
});