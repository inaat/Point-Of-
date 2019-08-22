from django.contrib import admin
from django.urls import path
from .views import  Home, organization,Product_Info,AccoundFind,ProjectCodeFind

app_name = 'accounts'
urlpatterns = [
    path('home/', Home, name='home'),
    path('organization/',organization, name='organization'),
    path('ProjectCodeFind/', ProjectCodeFind, name = 'ProjectCodeFind'),
    path('Product_Info/',Product_Info, name='Product_Info'),
    path('AccoundFind/', AccoundFind, name = 'accoundFind'),

    
]




 