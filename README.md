# Wells
![Wells logo](static/img/well.png)

Wells is a location enabled application dedicated to providing information and navigation directions to ancient water sources, latterly referred to as 'holy wells'.

All users have access to all the available information contained in the app as well as a handy location enabled map with markers to all the well locations in the database. In addition to the markers, some wells have separate information pages which can be accessed from the home page or from the map locations themselves via marker popup.

Registered users can like or add comments to any of the linked information pages and in addition, they can edit or delete their own comments but not comments made by other users. Staff users have the ability to moderate (approve) comments, can add information pages for wells which exist in the database and in cases where there is no existing record, can also add well location records to the database.

Each well record in the database includes the name of the well, the townland and county, the longitude and latitude, and cures associated with the well.

---

# Table of Contents

- [Wells](#wells)
- [Table of Contents](#table-of-contents)
- [Features](#features)
  - [Home Page](#home-page)
  - [About Page](#about-page)
  - [Map Page](#map-page)
  - [Authentication](#authentication)
- [Design](#design)
  - [DB Model](#database-model)
  - [Color Scheme](#general-color-scheme)
  - [Logo](#logo)
  - [Home](#home)
  - [About](#about)
  - [Map](#map)
    - [Popup](#popups)
  - [User Authentication](#user-authentication)
- [User Experience](#user-experience)
- [Testing](#testing)
  - [User Stories](#user-stories)
  - [Desktop](#desktop)
      - [Content Page](#content-page)
      - [Comments](#comments)
    - [About Page](#about-page-1)
    - [Map Page](#map-page-1)
    - [Authentication](#authentication-1)
  - [Tablet](#tablet)
      - [Content Page](#content-page-1)
      - [Comments](#comments-1)
    - [About Page](#about-page-2)
    - [Map Page](#map-page-2)
    - [Authentication](#authentication-2)
  - [Mobile](#mobile)
      - [Content Page](#content-page-2)
      - [Comments](#comments-2)
    - [About Page](#about-page-3)
    - [Map Page](#map-page-3)
    - [Authentication](#authentication-3)
  - [Map Interaction](#map-interaction)
- [Technologies](#technologies)
- [Credits](#credits)
- [Notes](#notes)
  - [Map Popup Dialog](#map-popup-dialog)

---

# Features

## Home Page

The home page contains links to pages with information and details about any wells for which a linked page exists. Not all wells have detailed information pages but every information page must have a corresponding well entry.

Each entry has a photograph of its related well and contains the author's name. Each post displays a brief excerpt from the page contents and the date on which the content page was created followed by a like (heart) icon, showing the numbber of page likes.

## About Page

The about page shows a historic painting depicing one of the wells and a general background or history of the subject matter.

## Map Page

The map page displays a scrollable and zoomable map with markers indicating the location of each well. Clicking the markers results in a popup with a link to the well information page, where one exists, and a button which when clicked open google maps centered on the related location marker. The user can then click on the 'directions' button in google maps to navigate to the entry from their current or chosen location.

## Authentication

Users can register an account in order to comment on the information pages. Existing users can login and logout and are presented with a link to login if they have not already done so or to logout if they are already logged in.

---

# Design

## Database Model

The wells databases utilizes three main models with relationships as shown in the following diagram. I've included the builtin Djano User model to showits relationships to the three models.

<details>
<summary>ERM</summary>

![ERM](/media/erm.png)

</details>

A well record must exist before a post can be created. When the post is saved, the well's *'townland'* and *'county'* fields are joined and saved as a single *'location'* field in the post, and the well's *'cures'* field is saved to the *'cures'* field in the post record.

## General Color Scheme

I used a very simple color scheme almost verging on black & white for simplicity and good color contrast. The navbar, footer, button elements and poat body text all use a charcoal colour while white is used for logos, icons, elements and text whcih have charcoal backgrounds.

<details>
<summary>Color Scheme</summary>

![Color Scheme](/media/color-scheme.png)

</details>

## Logo

The logo uses a water droplet and a celtic spiral which I tilted horizontally to give the impression of water ripples. 

## Home

I used the same basic layout as CI's "I think therefore I blog" tutorial with a slight alteration to the color pallet.

<details>

<summary>Homepage Laptop Mockup</summary>

![Homepage Laptop Mockup](/media/lap/homepage-large-mockup.png)

</details>

<details>

<summary>Mobile Laptop Mockup</summary>

![Homepage Mobile Mockup](/media/mob/mobile-homepage-mockup.png)

</details>

## About

Again simplicty is the order of the day for the about page which contains a single large image and information under a number of headings relating to the holy wells in general. 

## Map

The map uses the same page tempalate for the navigation bar and footer as the above mentioned pages but I opted to lock the footer so that it would remain in place while scrolling the map downwards. I used my logo for the markers for well locations.

### Popup

The popup uses the Mapbox popup element and I created a popup template which loads once the popup is clicked. My logo is used once again and the popup has a title matching the well name whcih becomes a link if there is a related post for that well. Below that is an excerpt from that post if it exists and at the bottom a button which opens the location in Google maps using the well's coordinates. More information relating to the map and popup functionality is contained in the [notes](#notes).

## User Authentication

---

# User Experience

User stories were created to aid in the planning of the site and for the agile tasks for the application project.

- As a staff user I can create location records so that markers will be available on the map
- As a staff user I can create a post so that users can get information about a well
- As a visitor I can read posts on the home page
- As a visitor I can read an about page to get some background
- As a visitor I can access a map page to see where wells are located
- As a visitor I can click on a well marker to open a popup
- As a visitor I can click on the popup title to read more information
- As a visitor I can click on a button in the popup to see the location in google maps
- As a user I can register on the site
- As a user I can like or unlike posts
- As a user I can add comments to information pages
- As a site user I can edit or delete my own comments
- As a staff user I can approve comments made by user

---

# Testing

## User Stories

Each user story has its own Agile task. In this way the implementation and the testing is integrated as one. A task may have dependencies which must be in place in order for the current task to be completed. An example of this is shown here.

<details>
<summary>Agile-Task</summary>

![Agile-Task](media/agile-task.png)

</details>

The following screenshots show the result of user actions on the various platforms. First we see the screenshots of various menu choices and internal content interactions for desktop or laptop devices, followed respectively by tablet devices and finally mobile phone devices. The testing indicates that content and pages are accessible on all formats.

The styling has been slightly changed since the screenshots were taken. The page now uses the same background color for the navigation bar, post title masthead, comment submit & edit buttons, and for all the authentication buttons.

&nbsp;

## Desktop

<details>
<summary>Home Page</summary>

![Home](media/lap/home.png)

</details>

#### Content Page

On clicking on any of the posts from the Home Page or on a link from the Map Page popup the user will then be able to view the content related to that item.

<details>
<summary>Content Page</summary>

![Home](media/lap/content.png)

</details>

#### Comments

Once in the content page a user may post, edit and delete their own comments. When a comment is posted or edited the user will see the post in greyed out text with a <span style="color: rgb(222, 146, 168);"> *'This comment is awaiting approval'* </span> message below the comment, indicating that the comment is waiting approval by a moderator.

<details>
<summary>Post Comment

</summary>

![Home](media/lap/comment-1.png)

</details>

<details>
<summary>Edit Comment

</summary>

![Home](media/lap/comment-2.png)

</details>

<details>
<summary>Delete Comment

</summary>

![Home](media/lap/comment-3.png)

</details>

### About Page

<details>
<summary>About Page</summary>

![Home](media/lap/about.png)

</details>

### Map Page

<details>
<summary>Map Page</summary>

![Home](media/lap/map.png)

</details>

### Authentication

<details>
<summary>Login Modal</summary>

![Home](media/lap/login.png)

</details>


<details>
<summary>Logout Modal</summary>

![Home](media/lap/logout.png)

</details>


<details>
<summary>Register Modal</summary>

![Home](media/lap/register.png)

</details>

&nbsp;

## Tablet

<details>
<summary>Home Page</summary>

![Home](media/tab/home-tab.png)

</details>

#### Content Page

On clicking on any of the posts from the Home Page or on a link from the Map Page popup the user will then be able to view the content related to that item.

<details>
<summary>Content Page</summary>

![Home](media/tab/content-tab.png)

</details>

#### Comments

Once in the content page a user may post, edit and delete their own comments. When a comment is posted or edited the user will see the post in greyed out text with a <span style="color: rgb(222, 146, 168);"> *'This comment is awaiting approval'* </span> message below the comment, indicating that the comment is waiting approval by a moderator.

<details>
<summary>Post Comment

</summary>

![Home](media/tab/comment-tab1.png)

</details>

<details>
<summary>Edit Comment

</summary>

![Home](media/tab/comment-tab2.png)

</details>

<details>
<summary>Delete Comment

</summary>

![Home](media/tab/comment-tab3.png)

</details>

### About Page

<details>
<summary>About Page</summary>

![Home](media/tab/about-tab.png)

</details>

### Map Page

<details>
<summary>Map Page</summary>

![Home](media/tab/map-tab.png)

</details>

### Authentication

<details>
<summary>Login Modal</summary>

![Home](media/tab/login-tab.png)

</details>


<details>
<summary>Logout Modal</summary>

![Home](media/tab/logout-tab.png)

</details>


<details>
<summary>Register Modal</summary>

![Home](media/tab/reg-tab.png)

</details>

&nbsp;

## Mobile

<details>
<summary>Home Page</summary>

![Home](media/mob/home-mob.png)

</details>

#### Content Page

On clicking on any of the posts from the Home Page or on a link from the Map Page popup the user will then be able to view the content related to that item.

<details>
<summary>Content Page</summary>

![Home](media/mob/content-mob.png)

</details>

#### Comments

Once in the content page a user may post, edit and delete their own comments. When a comment is posted or edited the user will see the post in greyed out text with a <span style="color: rgb(222, 146, 168);"> *'This comment is awaiting approval'* </span> message below the comment, indicating that the comment is waiting approval by a moderator.

<details>
<summary>Post Comment

</summary>

![Home](media/mob/comment-mob1.png)

</details>

<details>
<summary>Edit Comment

</summary>

![Home](media/mob/comment-mob2.png)

</details>

<details>
<summary>Delete Comment

</summary>

![Home](media/mob/comment-mob3.png)

</details>

### About Page

<details>
<summary>About Page</summary>

![Home](media/mob/about-mob.png)

</details>

### Map Page

<details>
<summary>Map Page</summary>

![Home](media/mob/map-mob.png)

</details>

### Authentication

<details>
<summary>Login Modal</summary>

![Home](media/mob/login-mob.png)

</details>


<details>
<summary>Logout Modal</summary>

![Home](media/mob/logout-mob.png)

</details>


<details>
<summary>Register Modal</summary>

![Home](media/mob/reg-mob.png)

</details>

&nbsp;


## Map Interaction

The map, with its markers indicating the locations of the wells, is really the main event in this application. The map itself uses [mapbox gl](https://www.mapbox.com/) and there are explanatory [notes](#notes) at the end of this document detailing how it(mapbbox), python and javascript all hangs together. The marker popup works in the same way on all devices and consists of three elements, Popup Title, Excerpt and a Google Maps Link to the loction.

The popup title is becomes an active link when there a related content record in the database or a plain heading when there is not. You can see the link to the post content appear in the bottom right of the screen in the Popup Title screenshot. By clicking on the <span style="color: rgb(168, 109, 0);">*'open location in google maps'*</span> button, a new google maps page opens with the location set as a destination allowing the user to click on the *'Directions'* link to navigate to the lcoation.

<details>
<summary>Popup Title</summary>

![Home](media/lap/popup-lnk1.png)

</details>

<details>
<summary>Google Map Link</summary>

![Home](media/lap/popup-lnk2.png)

</details>

<details>
<summary>Google Map Window</summary>

![Home](media/lap/gmap.png)

</details>

&nbsp;

---

# Technologies

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [JavaScript](https://www.javascript.com/): programming language.
- [Python 3](https://www.python.org/): programming language.
- [Django 3.2](https://www.djangoproject.com/)
  - [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/): for forms.
  - [Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/): bootstrap5 template pack for crispy forms.
  - [Django Forms Dynamic](https://github.com/dabapps/django-forms-dynamic): for the dynamic form using HTMX.
  - [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/): for the dynamic form.
  - [Coverage](https://github.com/nedbat/coveragepy/tree/6.5.0): for measuring code coverage of Python tests.

- [Bootstrap](https://getbootstrap.com/): styling.
- [Cloudinary](https://cloudinary.com/): store static and media files.
- [GIT](https://git-scm.com/): for version control.
- [GitHub](https://github.com/): for host repository.
  
- [Codeanywhere](https://codeanywhere.com/): online IDE.
- [Heroku](:<https://codeanywhere.com/): PaaS deployment site
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [Lucidchart](https://www.drawio.com/): for the mockups and ERM.
- [GIMP](https://www.gimp.org/): to create the logo

---

# Credits

---

# Notes

&nbsp;

## Map Popup Dialog


The map page is created using the 'map.html' template. Markers are placed on the map by the JSON data sent from the 'map.mapper' view which generates the data from the Well and related Post model records. When a marker is clicked the relevant variables are passed back to the 'map.popup' view which in turn generates the data for the popup dialog. The JS line in 'mapper.js' which passes the marker details is:

    var url = 'popup?title=' + encodeURIComponent(title) + '&post_slug=' + encodeURIComponent(post_slug) + '&coordinates=' + encodeURIComponent(r_coordinates.map(coord => Math.ceil(coord * 100000) / 100000).join(','));

The URL constructed in var url includes query parameters (title, post_slug, and coordinates). These query parameters are passed as part of the GET request to the server when the xhr.send() method is executed. This section of code creates the popup element using XMLHttpRequest to retrieve 'data' from the 'map.popup' view in this code:

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
