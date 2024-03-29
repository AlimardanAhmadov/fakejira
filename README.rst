django-fakejira test python library
===================================

This is sample code used in the Real Python article [Writing an Installable Django App](???). The article describes how to take an app from an existing Django project and make it a stand-alone installable package available on PyPI.

Installable App
---------------

This app can be installed and used in your django project by:

.. code-block:: bash

    $ pip install fakejira


Edit your `settings.py` file to include `'fakejira'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'fakejira',
    ]


Edit your project `urls.py` file to import the URLs:


.. code-block:: python

    url_patterns = [
        ...

        path('fakejira/', include('main.urls')),
    ]


Finally, add the models to your database:


.. code-block:: bash

    $ ./manage.py makemigrations fakejira

