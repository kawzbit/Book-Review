from . import views as bookViews
from django.urls import path

urlpatterns = [
    path('<int:book_id>', bookViews.detail, name ='detail' )
]