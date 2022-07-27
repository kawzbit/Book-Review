from django.urls import path
from . import views as accountsviews

urlpatterns = [path("signupaccount/", accountsviews.signupaccount, name="signupaccount")]



