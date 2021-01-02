This package provides subclasses modifying the django-allauth views https://github.com/pennersr/django-allauth so they can work with Turbo Streams for form validation. The package django-turbo-response https://github.com/hotwire-django/django-turbo-response is used to provide the required mixin classes.

This package is required in order to provide allauth compatability with Turbo. Turbo form validation requires that validation errors be returned in a Turbo Stream response.

**Disclaimer**: the Hotwired/Turbo client libraries are, at time of writing, still in Beta. We expect there will be breaking changes until the first stable release. This package, and the Turbo client, should therefore be used with caution in a production environment. The version used in testing is *@hotwired/turbo==7.0.0-beta.1*.

## Requirements

This library is tested for Python 3.8+.

## Installation

> pip install django-turbo-allauth

To install from Git:

> git clone https://github.com/danjac/django-turbo-allauth

> cd django-turbo-allauth

> python setup.py install

**Note**: This library does not include any client libraries (Turbo or Stimulus). You may wish to add these yourself using your preferred Javascript build tool, or use a CDN. Please refer to the Hotwire documentation on installing these libraries.

Full documentation on ReadTheDocs:

https://django-turbo-allauth.readthedocs.io/en/latest/


## License

This project is covered by the MIT license.



