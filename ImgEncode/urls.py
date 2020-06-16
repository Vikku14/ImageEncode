from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Encode import api_views
from Encode import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Encode.urls')),
    # path('api/', views.apiOverview, name = 'overview'),


    path('api/image-api', views.ImageApi.as_view(), name= 'image-api'),

]
