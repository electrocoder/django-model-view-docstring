===========================
Django Model View Docstring
===========================

Django app model and views docstring. Django is the most powerful framework for Python. For the applications we create, it takes the docstrings of the models and views and lists them at admin/model-view-helper/

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "model_view_docstring" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'model_view_docstring',
    ]

2. Include the model_view_docstring URLconf in your project urls.py like this::

    path('admin/model-view-docstring/', include('model_view_docstring.urls')),

3. Run ``python manage.py migrate`` to create the model_view_docstring models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

5. Visit http://127.0.0.1:8000/admin/model-view-helper/ to model and view helper.




