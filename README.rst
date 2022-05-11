django-fakejira-testing-app-1
=============================

This is a installable Django App that allows users to add e-commerce products and view their statuses on a workflow chart. It's also available on PyPI.

Installable App
---------------

This app models a list of items on a receipt. Each item has a description and a cost. A receipt may reference multiple items.

This app can be installed and used in your django project by:

.. code-block:: bash

    $ pip install django-fakejira-testing-app-1


Edit your `settings.py` file to include `'fakejira1'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'fakejira1',
    ]


Edit your project `urls.py` file to import the URLs:


.. code-block:: python

    url_patterns = [
        ...

        path('/', include('fakejira1.urls')),
    ]


Finally, add the models to your database:


.. code-block:: bash

    $ ./manage.py migrate fakejira1

