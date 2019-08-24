from django.contrib import admin
from django.urls import path
from .views import  Home, organization,AccoundFind,ProjectCodeFind,Account_List_By_Type

app_name = 'accounts'
urlpatterns = [
    path('home/', Home, name='home'),
    path('organization/',organization, name='organization'),
    path('ProjectCodeFind/', ProjectCodeFind, name = 'ProjectCodeFind'),
    
    path('AccoundFind/', AccoundFind, name = 'accoundFind'),
    path('Account_List_By_Type/',Account_List_By_Type, name= 'Account_List_By_Type')

    
]




 