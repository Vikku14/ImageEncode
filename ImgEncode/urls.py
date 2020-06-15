from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Encode import api_views

router = routers.DefaultRouter()
router.register('imagedata', api_views.ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Encode.urls')),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

]
