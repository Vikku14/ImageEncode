from django.contrib import admin
from django.urls import path, include


from Encode import views
from Encode.api import views as vs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Encode.urls')),
    path('api/image-api', vs.ImageApi.as_view(), name= 'image-api'),

]
