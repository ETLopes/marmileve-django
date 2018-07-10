from django.urls import path

from sitemarmileve.views import index


urlpatterns = [
    path('', index, name='index')
]