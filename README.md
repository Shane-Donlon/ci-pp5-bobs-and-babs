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

![error message for print statement used](documentation/assets/vs-code-extension-error-print-statement.jpg)

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

  <summary>Sign up</summary>

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

![Sign-out page](documentation/assets/logout-page.jpg)

</details>

<details >

  <summary>Customer Orders</summary>

![Customer Orders Page](documentation/assets/customer-orders.jpg)

![Order in progress page](documentation/assets/order-wip.jpg)

![Order Complete Delivery page](documentation/assets/order-complete-delivery.jpg)

![Order Complete Collection page](documentation/assets/order-complete-collection.jpg)

</details>

<details >

  <summary>Admin Add Products</summary>

![Admin Add products form](documentation/assets/admin-add-products.jpg)
Note product name was "test"

![Admin Add products named test](documentation/assets/product-named-test.jpg)

![Admin Add products added sucecss](documentation/assets/product-add-success.jpg)

</details>

<details >

  <summary>Admin Update Products</summary>

![Admin update products form](documentation/assets/admin-update-products.jpg)
![Admin update products success](documentation/assets/product-update-success.jpg)

</details>
<details >

  <summary>Admin Remove Products</summary>

![Admin Delete products table](documentation/assets/admin-del-products.jpg)
![Admin Delete products form](documentation/assets/admin-delete-products-page.jpg)
![Admin Delete products confirmation](documentation/assets/delete-confirm-request.jpg)
![Admin Delete products success](documentation/assets/product-delete-success.jpg)

</details>

<details>
  <summary>Admin Order Fulfillment</summary>

![Admin Orders table](documentation/assets/admin-orders-table.jpg)
![Admin Orders form page](documentation/assets/admin-order-fulfillment.jpg)
![Admin Orders fulfilled success](documentation/assets/order-fulfiled.jpg)

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

### Python validation:

While the Python code has been validated an error persists on the validation tool
This error is due to the fact that I'm using this to render a pattern in HTML using Django and Regex.

While this is invalid for python the code is valid HTML REGEX Pattern

![Python validation error](documentation/assets/line-40-invalid-invalid-msg.jpg)

Offending Code:
This code is for Client Side Validation of Eircodes
Not strictly needed, but this client-side validation was a struggle with Project 4 and wanted to implement again for Project 5.
As I have more experience and wanted to re-visit some implementations from the past.

The regex is to allow 1231234 and 123 1234 to be accepted as eircode.

```python
'pattern': '[A-Za-z0-9]{3}\s*[A-Za-z0-9]{4}'
```

### CSS Validation:

I opted to use container queries in this project in order to gain a better understanding of them, this has led to some css validation issues with the validator the CSS used is valid, but the validator has not yet been upated to inspect this level 3 CSS

#### base.css file

![CSS validation error](documentation/assets/css-error.jpg)

#### home.css file

![CSS validation error](documentation/assets/css-error-2.jpg)

#### checkout.css file

![CSS validation error](documentation/assets/css-error-3.jpg)

#### cart.css file

![CSS validation error](documentation/assets/css-error-4.jpg)

All other css files are clear of errors

### HTML Validation:

#### home.html

This error is from Adobe In-design product

![HTML validation error](documentation/assets/html-error-1.jpg)

Under accessibility guidelines decorative images can either have a blank alt attribute or role presentation, this is for the grey svg on the homepage and is not an error, it's more that the context isn't checked

![HTML validation error](documentation/assets/html-error-2.jpg)

#### sign up page

Error is from allauth templates
this happened for Project 4 and I was unable to resolve this

![HTML validation error](documentation/assets/html-error-3.jpg)

#### sign in page

Error is from allauth templates
this happened for Project 4 and I was unable to resolve this

![HTML validation error](documentation/assets/html-error-4.jpg)

#### profile update page

empty option is coming from Django loop
street address autocomplete is valid for this context of using "Town"

![HTML validation error](documentation/assets/html-error-5.jpg)
