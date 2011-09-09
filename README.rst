Django-Tumblr-Auth
==============================

Django-Tumblr-Auth is an extension to `Django-Social-Auth <https://github.com/omab/django-social-auth>`_
which adds a backend for Tumblr.com.


Requirements
-------------------------------

- Django-Social-Auth >= 0.3.3
    - Django >= 1.2.5
    - Python-OAuth >= 1.0.1


API Keys
-------------------------------

In order to use this application you must sign up for OAuth consumer key on
http://www.tumblr.com/oauth/apps. These should be put into your settings file
using the settings::

    TUMBLR_CONSUMER_KEY = '' # Your consumer key
    TUMBLR_CONSUMER_SECRET = '' # Your consumer secret


Installation
-------------------------------

To install django-tumblr-auth via pip::

    pip install django-tumblr-auth

Or you can from the latest version from Github manually::

    git clone git://github.com/alageek/django-tumblr-auth.git
    cd django-tumblr-auth
    python setup.py install

or via pip::

    pip install -e git+https://github.com/alageek/django-tumblr-auth.git

Once you have the app installed you must include in your settings::

    INSTALLED_APPS = (
        ...
        'social_auth',
        'tumblr_auth',
        ...
    )

    AUTHENTICATION_BACKENDS = (
        ...
        'tumblr_auth.backend.TumblrBackend',
        ...
    )

    SOCIAL_AUTH_IMPORT_BACKENDS = (
        ...
        'tumblr_auth',
        ...
    )

Please refer to the `Django-Social-Auth <http://django-social-auth.readthedocs.org/>`_
documentation for additional information.


Questions or Issues?
-------------------------------

If you have questions, issues or requests for improvements please let me know on
`Github <https://github.com/mlavin/django-tumblr-auth/issues>`_.
