![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

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
