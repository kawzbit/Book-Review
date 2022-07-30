from . import views as bookViews
from django.urls import path

urlpatterns = [
    path('<int:book_id>', bookViews.detail, name ='detail' ),
    path('<int:book_id>/create', bookViews.createreview, name ='createreview' ),
    path('review/<int:review_id>', bookViews.updatereview, name ='updatereview' ),
    path('review/<int:review_id>/delete', bookViews.deletereview, name ='deletereview' ),
]