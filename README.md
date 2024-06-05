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

<details>

  <summary>Homepage</summary>

![Homepage of website](documentation/assets/home-page-bobs-and-babs.jpg)

</details>

<details >

  <summary>Shop</summary>

![Shop page of website](documentation/assets/shop-page.jpg)

</details>

<details>

  <summary>Product</summary>
It was important to route to this page as part of the add to cart option to ensure the allergin information is seen

![Shop page of website](documentation/assets/product-page.jpg)
![Loading Spinner of website](documentation/assets/loading-spinner.jpg)
![Add to cart success message](documentation/assets/loading-spinner.jpg)
![Add to cart success message](documentation/assets/added-to-cart.jpg)
![Add to cart failure message](documentation/assets/added-to-cart-failure.jpg)

</details>

<details >

  <summary>Cart</summary>

![Cart page of website](documentation/assets/cart-page.jpg)

</details>

<details >

  <summary>Checkout Page Delivery</summary>

![checkout page of website delivery status](documentation/assets/checkout-page-delivery.jpg)

</details>

<details >

  <summary>Checkout Page Collection</summary>

![checkout page of website collection status](documentation/assets/checkout-page-collection.jpg)

</details>

<details >

  <summary>Order Success</summary>

![checkout page of website collection status](documentation/assets/checkout-page-order-complete.jpg)

</details>

<details >

  <summary>Order Failure</summary>

![checkout page of website collection status](documentation/assets/checkout-page-order-failed.jpg)

</details>

<details >

  <summary>Form Validation</summary>

![form validation phone number error](documentation/assets/form-validation-phone.jpg)

![form validation eircode error](documentation/assets/form-validation-eircode.jpg)

</details>

<details >

  <summary>Signup</summary>

![Sign-up page](documentation/assets/sign-up-page.jpg)

![Verify Email Page](documentation/assets/verify-email.jpg)

![Verify Email Received](documentation/assets/verify-email-received.jpg)

![Verify Email Site ID](documentation/assets/email-site-id.jpg)

</details>

<details >

  <summary>Sign In</summary>

![Sign in page](documentation/assets/sign-in-page.jpg)

</details>

<details >

  <summary>Profile Page</summary>
Where "Prefilled" is the email address used to sign up (hidden for screenshots)

![Profile Page](documentation/assets/update-profile-page.jpg)

![Profile Page success](documentation/assets/profile-updated.jpg)

</details>

<details >

  <summary>Logout Page</summary>

</details>

### Wireframes & Styling

![Adobe XD Wireframes](documentation/assets/adobe-xd-wireframes.jpg)

![Adobe XD Styles](documentation/assets/adobe-xd-styles.jpg)

### Entity Relationship Diagram (ERD)

![ERD Diagram](documentation/assets/erd.jpg)

- Order Items holds the indiviaul products per order
- Shipping information holds all shipping information (which may or may not include a customer)
  The reason for this is to support unauthenticated users

### Unauthenticated Users

This site supports purchases from unauthenticated users.

This is supported by creating and storing a session key
This session key is stored in the 'users session', and is used to store the cart items for the user
If the user starts unauthenticated then logs in or creates an account the order is transferred over to the customer order
if a current order exists the items are added to the current order and the unauthenticated order is removed

The use of session keys also works along with closing browser or navigating away from the page

Please note this feature will not work in incognito mode as this clears the session key on browser exit

### Improvements:

I would like to add the GDPR Banner for cookies,
While all cookies are purely functional it is still a requirement to add this,
also the fact that the site uses authentication is another reason to include this banner as Django uses session keys to track authenticated users
