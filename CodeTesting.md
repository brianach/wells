# Testing

### [HTML Validator](https://validator.w3.org/)

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

![Home Page](/media/testing/home.png)
</details>

### Post Details

<details>
<summary>Post Details</summary>

![Post Details](/media/testing/post_detail.png)
</details>

## About

<details>
<summary>About Page</summary>

![About Page](/media/testing/about.png)
</details>

## Map

<details>
<summary>Map Page</summary>

![Map Page](/media/testing/map.png)
</details>

### Popup

<details>
<summary>Location Popup</summary>

![Popup](/media/testing/popup.png)
</details>

One warning for the popup template.

&nbsp;

### [CSS Validator](https://jigsaw.w3.org/css-validator/)

All CSS pages passed the W3C CSS Validation Service

![CSS Validation](/media/testing/css/css.png)

&nbsp;

## JavaScript Testing

JSHint was used for validating the JavaScript. 