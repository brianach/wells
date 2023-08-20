# Testing

Code testing and validation tests, user story testing and user acceptance testing.

## Table of Contents

- [Testing](#testing)
  - [Table of Contents](#table-of-contents)
    - [HTML Validation](#html-validation)
  - [Templates](#templates)
    - [Accounts templates](#accounts-templates)
    - [Error page templates](#error-page-templates)
  - [Home](#home)
    - [Post Details](#post-details)
  - [About](#about)
  - [Map](#map)
    - [Popup](#popup)
    - [CSS Validator](#css-validator)
  - [JavaScript Testing](#javascript-testing)
  - [Python Testing](#python-testing)
  - [User Story Testing](#user-story-testing)
    - [Map Interaction](#map-interaction)
    - [Authentication](#authentication)
    - [Post Interaction](#post-interaction)
  - [UAT on all devices](#uat-on-all-devices)
  - [Bugs](#bugs)

&nbsp;

---

### [HTML Validation](https://validator.w3.org/)

HTML was validated by copying the page source and pasting into the validator and by entering the link in the validator.

## Templates

### Accounts templates

<details>
<summary>login template</summary>
![login](/media/testing/html/login.png)
</details>

<details>
<summary>logout template</summary>

![logout](/media/testing/html/logout.png)
</details>

<details>
<summary>signup template</summary>

![signup](/media/testing/html/signup.png)
</details>

One error was generated in the logout template but unresolvable because it is jinja related.

### Error page templates

<details>
<summary>err400 template</summary>

![err400](/media/testing/errors/err400.png)
</details>

<details>
<summary>err403 template</summary>

![err403](/media/testing/errors/err403.png)
</details>

<details>
<summary>err404 template</summary>

![err404](/media/testing/errors/err404.png)
</details>

<details>
<summary>err405 template</summary>

![err405](/media/testing/errors/err405.png)
</details>

<details>
<summary>err500 template</summary>

![err500](/media/testing/errors/err500.png)
</details>

Two identical errors were generated in the each of the error page template but unresolvable because they are jinja related.

## Home

<details>
<summary>Home Page</summary>

![Home Page](/media/testing/html/home.png)
</details>

### Post Details

<details>
<summary>Post Details</summary>

![Post Details](/media/testing/html/post_detail.png)
</details>

## About

<details>
<summary>About Page</summary>

![About Page](/media/testing/html/about.png)
</details>

## Map

<details>
<summary>Map Page</summary>

![Map Page](/media/testing/html/map.png)
</details>

### Popup

<details>
<summary>Location Popup</summary>

![Popup](/media/testing/html/popup.png)
</details>

One warning for the popup template.

&nbsp;

### [CSS Validator](https://jigsaw.w3.org/css-validator/)

All CSS pages passed the W3C CSS Validation Service

![CSS Validation](/media/testing/css/css.png)

&nbsp;

## JavaScript Testing

JSHint was used for validating the JavaScript.

## [Python Testing](https://extendsclass.com/python-tester.html)

ExtendsClass was used to validate the python code. Two errors were reported out of all the code. However the errors are due to the checker running an older version of Python which doesn't support f-strings.

![reported error](/media/testing/tobar_admin.png)

&nbsp;

---

## User Story Testing

### Map Interaction

View and click on well locations on a map  
<https://github.com/brianach/wells/issues/11>

### Authentication

Signup, signin and signout  
<https://github.com/brianach/wells/issues/14>

### Post Interaction

Like posts  
<https://github.com/brianach/wells/issues/16>

Post comments  
<https://github.com/brianach/wells/issues/15>

Edit or delete comments  
<https://github.com/brianach/wells/issues/20>

## UAT on all devices

Desktop or Laptop UAT  
<https://github.com/brianach/wells/issues/23>

Tablet UAT  
<https://github.com/brianach/wells/issues/24>

Smartphone UAT  
<https://github.com/brianach/wells/issues/25>

&nbsp;

---

## Performance

### Home Page

<details>
<summary>Home Page Performance</summary>

![hpp](/media/lighthouse/home-page-perf.png)
</details>

### About Page

<details>
<summary>About Page Performance</summary>

![app](/media/lighthouse/about-page-perf.png)
</details>

### Map Page

<details>
<summary>Map Page Performance</summary>

![mpp](/media/lighthouse/map-page-perf.png)
</details>

### Post Detail

<details>
<summary>Map Page Performance</summary>

![dpp](/media/lighthouse/post-detail-perf.png)
</details>

&nbsp;

---

## Bugs

The following bugs and issues were encoutered and resolved

- [Issue with selecting location data](https://github.com/brianach/wells/issues/10)
- [MIME type issue on Heroku deployment](https://github.com/brianach/wells/issues/12)
- [Popups not working on mobile device](https://github.com/brianach/wells/issues/13)
- ['maximum recursion depth exceeded' error](https://github.com/brianach/wells/issues/17)
- [Heroku deployment failure due to slug size](https://github.com/brianach/wells/issues/18)
- [Collectstatic whitenoise errors](https://github.com/brianach/wells/issues/28)
- [Server 500 error when loading post details after deployment](https://github.com/brianach/wells/issues/29)
- [Fix issue where the navigation bar is hiding geolocation button on map page](https://github.com/brianach/wells/issues/30)

Unresolved bug

- A new or an existing post can be linked to a well which is already linked. However this can only be done by an superuser or staff user on the admin backend. Such a user would or should be aware of this.
