[link to deployed site](https://sd-ci-pp5-bobs-and-babs-5fa3ca5e7225.herokuapp.com/)

# Bob & Bab's e-commerce website

Bob & Babs website is a store that sells freshly baked goods in the Dublin Area.
This has been built using Django, HTML, CSS and JavaScript, stripe and is hosted on Heroku.
AdobeXD was also used for the low-fidelity wireframes, and Photoshop for the assets.

## Site goals:

- Sell freshly baked goods to the Dublin Area
- Provide delivery and collection services
- Provide a user-friendly experience
- Provide a secure payment system

## Technologies Used:

### Languages:

- HTML
- CSS
- JavaScript
- Python
- Django
- Node.JS
- Powershell

Node.JS was used to create bespoke VSCode Extensions to improve my Developer Experience with Django.
Django Custom Commands Extension was created to allow me to run Django Custom Commands from within VSCode.

### Django Custom Commands Extension:

This allowed me to utilise Python to create and update Apps with ease.
On new app creation the extension will automatically create the necessary files, and folders for the app.
As well as migrate all the template tags from the base.html file into the current HTML file.

![Code Snippet from Custom Extension](documentation/assets/django-custom-commands-extension-createApp.jpg)

![VSCode Extension input asking for app name](documentation/assets/create-app-app-name.jpg)
![VSCode Extension input appname testing](documentation/assets/app-name-testing.jpg)
![VSCode Extension Files Created](documentation/assets/testing-app-files-add.jpg)
![VSCode Extension Files HTML File input](documentation/assets/testing-html-file.jpg)

The extension would also update the base urls.py file to include the new app's url.
This would then update my settings.py file installed apps to include the new application
This also allowed me to create custom commands to run from the terminal in VSCode, and adding keyboard shortcuts to run these commands.

As well as to automatically comment on closing divs, and section tags in html files using beautiful soup as the HTML parser.

### Githooks:

Custom githooks were created for commit-msg and pre-push hooks
The purpose of these hooks were to ensure that the commit message was in the correct format, and that I was informed of an attempt to push debug code, conosle.log(), print() statements appropriately.

Powershell was used to create the hooks, and the hooks were stored in the hooks folder in the root directory of the project.

![Hooks Folder with sample hooks and commit-msg and pre-push hooks being used](documentation/assets/hooks.jpg)

![commit-msg error](documentation/assets/commit-msg-hook.jpg)

### Tools:

- Github
- Githooks

### Libraries:

- allauth
- django_browser_reload
- cloudinary
- django-tables2
- stripe
- sendgrid
- typing_extensions
- gunicorn
- whitenoise
- dj-database-url
- psycopg2-binary

### Hosting:

Heroku

### Features:

<details open>

  <summary>Homepage</summary>

![Homepage of website](documentation/assets/home-page-bobs-and-babs.jpg)

</details>

<details open>

  <summary>Shop</summary>

![Shop page of website](documentation/assets/shop-page.jpg)

</details>

It was important to route to this page as part of the add to cart option to ensure the allergin information is seen

<details open>

  <summary>Product</summary>

![Shop page of website](documentation/assets/product-page.jpg)
![Loading Spinner of website](documentation/assets/loading-spinner.jpg)
![Add to cart success message](documentation/assets/loading-spinner.jpg)
![Add to cart success message](documentation/assets/added-to-cart.jpg)
![Add to cart failure message](documentation/assets/added-to-cart-failure.jpg)

</details>
