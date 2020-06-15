from django.urls import path
from . import views


app_name='Encode'
urlpatterns = [
    path('', views.picture, name='picture')
]
