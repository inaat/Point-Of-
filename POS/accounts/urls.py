from django.contrib import admin
from django.urls import path
from .views import  Home, organization,Product_Info,postContact

app_name = 'accounts'
urlpatterns = [
    path('home/', Home, name='home'),
    path('organization/',organization, name='organization'),
    #path('ajax/get_user_info', getUserInfo, name = 'get_user_info'),
    path('Product_Info/',Product_Info, name='Product_Info'),
    path('AccoundFind/', AccoundFind, name = 'accoundFind'),

    
]