from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'sesion'
urlpatterns = [
    path('create/', create_session , name='create'),
    path('access/', access_session),
    path('del/', delete_session )
]