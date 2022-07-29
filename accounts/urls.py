from django.urls import path
from . import views as accountsviews

urlpatterns = [
    path("signupaccount/", accountsviews.signupaccount, name="signupaccount"),
    path('logout/', accountsviews.logoutaccount,name='logoutaccount'), 
    path('login/', accountsviews.loginaccount,name='loginaccount'), 
    ]



