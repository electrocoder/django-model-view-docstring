from django.urls import include, path

from model_view_docstring import views

urlpatterns = [
    path('', views.model_view_docstring),
]
