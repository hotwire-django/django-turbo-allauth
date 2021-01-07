This package provides subclasses modifying the `django-allauth views <https://github.com/pennersr/django-allauth>`_ views in order to return valid return codes for use with Turbo.

This package is required in order to provide allauth compatability with Turbo. Turbo form validation either setting the attribute *data-turbo="false"* in the form, or returning a 4** response. This provides subclasses for the latter.


**Disclaimer**: the Hotwired/Turbo client libraries are, at time of writing, still in Beta. We expect there will be breaking changes until the first stable release. This package, and the Turbo client, should therefore be used with caution in a production environment. The version used in testing is *@hotwired/turbo==7.0.0-beta.2*.

============
Requirements
============

This library is tested for Python 3.8+.

===============
Getting Started
===============

``pip install django-turbo-allauth``

To install from Git:

``git clone https://github.com/hotwire-django/django-turbo-allauth``

``cd django-turbo-allauth``

``python setup.py install``

**Note**: This install does not include any client libraries (Turbo or Stimulus). You may wish to add these yourself using your preferred Javascript build tool, or use a CDN. Please refer to the Hotwire documentation on installing these libraries.

Make sure to add **allauth.account** and **allauth.socialaccount** to **INSTALLED_APPS** as per the all-auth installation instructions. If you wish to use the default templates, you should also add **turbo_allauth** *before* these two apps:


.. code-block:: python

    INSTALLED_APPS = [
        ...
        "turbo_allauth",
        "allauth.account",
        "allauth.socialaccount",
    ]

Finally add this to your url configuration:


.. code-block:: python

   urlpatterns = [
       ...
      path("account/", include("turbo_allauth.urls")),
   ]

This will also include all the allauth views.


==========
Subclasses
==========

This package provides subclasses and template changes for the existing allauth views. Currently these views will not work with Turbo as form validation requires returning responses with a 422 status if validation fails and a 303 on redirect.

The following subclasses have been added:

- **turbo_allauth.views.account.LoginView**
- **turbo_allauth.views.account.SignupView**
- **turbo_allauth.views.account.EmailView**
- **turbo_allauth.views.account.PasswordChangeView**
- **turbo_allauth.views.account.PasswordSetView**
- **turbo_allauth.views.account.PasswordResetView**
- **turbo_allauth.views.account.PasswordResetFromKeyView**
- **turbo_allauth.views.socialaccount.PasswordSignupView**

Please consult the django-allauth documentation on how to further customize your authentication workflows.
