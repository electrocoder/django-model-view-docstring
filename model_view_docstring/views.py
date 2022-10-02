from django.shortcuts import render
from django.urls import URLPattern
from django.conf import settings

import django.apps


def model_view_docstring(request):
    """model_view_docstring"""
    # Exclude Django default models.
    exclude_models = ['LogEntry', 'Permission', 'Group', 'User', 'ContentType', 'Session']
    HELPER = []

    # All model list
    for i in django.apps.apps.get_models():
        if not i.__name__ in exclude_models:
            HELPER.append({"type": i.__module__, "name": i.__name__, "docstring": (i.__doc__).replace("\n", "</br>")})

    # All view list
    root_urlconf = __import__(settings.ROOT_URLCONF) 
    all_urlpatterns = root_urlconf.urls.urlpatterns 

    for pattern in all_urlpatterns:
        if isinstance(pattern, URLPattern):
            view_name =  pattern.callback.__name__  # get the view name
            view_docstring = pattern.callback.__doc__  # get the view doc
            HELPER.append({"type": pattern.callback.__module__, "name": view_name, "docstring": str(view_docstring).replace('\n', '</br>')})

    context = {
        'helper': HELPER,
    }
    return render(request, 'model_view_docstring/model_view_docstring.html', context)
