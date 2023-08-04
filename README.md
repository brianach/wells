![Wells logo](static/img/well.png) 

# Wells 

Wells is a location enabled application dedicated to providing information and navigation directions to ancient water sources, latterly referred to as 'holy wells'.

All users have access to all the available information contained in the app as well as a handy location enabled map with markers to all the well locations in the database. In addition to the markers, some wells have separate information pages which can be accessed from the home page or from the map locations themselves via marker popup.

Registered users can like or add comments to any of the linked information pages and in addition, they can edit or delete their own comments but not comments made by other users. Staff users have the ability to moderate (approve) comments, can add information pages for wells which exist in the database and in cases where there is no existing record, can also add well location records to the database.

Each well record in the database includes the name of the well, the townland and county, the longitude and latitude, and cures associated with the well.

---

# Table of Contents

- [Features](#features)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Map Page](#map-page)
    - [Authentication](#authentication)

- [Design](#design)
    - [Home](#home)
    - [About](#about)
    - [Map](#map)
    - [User Authentication](#user-authentication)

- [User Experiece](#user-experience)
- [Testing](#testing)
- [Technologies](#technologies)
- [Credits](#credits)

---

# Features
## Home Page
## About Page
## Map Page
## Authentication
---
# Design
## Home
## About
## Map
## User Authentication
---
# User Experience

## User Stories

User stories were created to aid in the planning of the site and for the agile tasks in the implementation of the applicationh.

- As a staff user I can create location records so that markers will be available on the map
- As a staff user I can create a post so that users can get information about a well
- As a user I can read posts on the home page
- As a user I can read an about page to get some background 
- As a user I can access a map page to see where wells are located
- As a user I can click on a well marker to get more details
- As a user I can click on the popup title to read more information
- As a user I can click on a button in the popup to see the location and navigate to it in google maps
- As a user I can register so that I can post comments
- As a user I can like or unlike posts
- As a user I can add comments to well information pages
- As a site user I can edit or delete my own comments


---
# Testing
---
# Technologies
---
# Credits


To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!

How the Map Popup Dialog is constucted:

The map page is created using the 'map.html' template. Markers are placed on the map by the JSON data sent from the 'map.mapper' view which generates the data from the Well and related Post model records.

When a marker is clicked the relevant variables are passed back to the 'map.popup' view which in turn generates the data for the popup dialog. The JS line in 'mapper.js' which passes the marker details is:

        var url = 'popup?title=' + encodeURIComponent(title) + '&post_slug=' + encodeURIComponent(post_slug) + '&coordinates=' + encodeURIComponent(r_coordinates.map(coord => Math.ceil(coord * 100000) / 100000).join(','));

The URL constructed in var url includes query parameters (title, post_slug, and coordinates). These query parameters are passed as part of the GET request to the server when the xhr.send() method is executed.
this section of code creates the popup element using XMLHttpRequest to retrieve 'data' from the 'map.popup' view in this code:

    xhr.open('GET', url);
    xhr.onload = function () {
        if (xhr.status === 200) {
            var data = xhr.responseText; // store the response text in a variable called data
            new mapboxgl.Popup().setLngLat(coordinates).setHTML(data).addTo(map);
        } else {
            console.error('Request failed.  Returned status of ' + xhr.status);
        }
    };

The 'map.popup' view is below and you can see that the variable used match those in the 'map.mapper' view as well as the mapper.js script:

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

The data passed back contains 'post_url' which combined with the popup title creates a link to the related marker post url defined by the 'tobar.PostDetail view below:

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "location": post.location,
                "comments": comments,
                "liked": liked,
            },
        )

This is the same view used for reading the posts from the home page.
