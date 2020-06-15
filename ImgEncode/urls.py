from django.contrib import admin
from django.urls import path, include


app_name='Encode'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Encode.urls'))
]
