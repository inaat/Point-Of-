from django.contrib import admin
from django.urls import path
from .views import Login, login_session,lousy_secret

app_name = 'genprocandfunctions'
urlpatterns = [
    path('',lousy_secret, name='lousy_secret'),
    path('login/', Login, name='Login'),
    path('see/',login_session, name='login_session')
]