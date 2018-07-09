from django.urls import path

from . import views

app_name = 'sitemarmileve'

urlpatterns = [
    path('', views.Index, name='index')
]