from django.urls import path
from . import views as newsViews

urlpatterns= [
    path('', newsViews.news, name = 'news'),
    ]