from django.contrib import admin
from django.urls import path
from .views import Product_Info
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Products'
urlpatterns = [
    path('Product_Info/',Product_Info, name='Product_Info'),
   
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                          
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)